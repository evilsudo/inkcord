from dataclasses import MISSING
import typing
import datetime
from ..resourceid import ResourceID
from .permissions import PermissionOverwrite, Permissions
from .user import User

class ThreadMetadata:
    def __init__(self, _data: dict):
        self.archived: bool = _data["archived"]
        """Whether this thread is archived or not."""
        self.auto_archive_duration: int = _data["auto_archive_duration"]
        """The duration, in minutes, in which this thread will auto archive itself. Only values this can be are 60,1440,4320, and 10080."""
        self.archive_timestamp: datetime.datetime = datetime.datetime.fromisoformat(
            _data["archive_timestamp"]
        )
        """The timestamp at which this thread's archive status last changed."""
        self.locked: bool = _data["locked"]
        """Whether this thread is locked"""
        self.invitable: bool | None = _data.get("invitable")
        """Whether other normal users can add other normal users to this thread."""


class Channel:
    """An object that represents a channel in any context. This is the class of with the other classes with a suffix of `Channel` inherit from."""

    def __init__(self, data: dict):
        """Creates a channel. Don't use this for creating a channel, it's a internal initialization function."""
        self._data = data

    @property
    def id(self) -> ResourceID:
        """The id of the channel."""
        return ResourceID(self._data["id"])

    @property
    def guild_id(self) -> ResourceID | None:
        """The ID of the guild that has this channel in it, if applicable."""
        if (_id := self._data.get("guild_id")) is not None:
            return ResourceID(_id)

    @property
    def position(self) -> int | None:
        """The position of this channel in the guild."""
        return self._data["position"] if self._data.get("position") else None

    @property
    def overwrites(self) -> list[PermissionOverwrite] | None:
        """The overwrites that are exclusive to this specific channel."""
        return (
            [
                PermissionOverwrite(overwrite)
                for overwrite in self._data["permission_overwrites"]
            ]
            if self._data.get("permission_overwrites")
            else None
        )

    @property
    def name(self) -> str | typing.Any:
        """The name of this channel. Returns MISSING if not found."""
        return self._data.get("name",MISSING)


    @property
    def topic(self) -> str | None:
        """The channel topic. Can be 4096 characters max on Forum and Media channels, and 1024 for all other channels. May be None."""
        return self._data["topic"] if self._data.get("topic") else None

    @property
    def last_message_id(self) -> ResourceID | None:
        """The most recent message in this channel's ID. May be None, if in a non text channel."""
        if (_id := self._data.get("last_message_id")) is not None:
            return ResourceID(_id)
    @property
    def slowmode(self) -> int | None:
        """The amount of seconds a user/bot has to wait before sending another message. May be None."""
        return self._data.get("rate_limit_per_user")

    @property
    def parent_id(self) -> ResourceID | None:
        """The id of the parent category for a Text Channel, for threads, the id of the text channel this thread was created."""
        if (_id := self._data.get("parent_id")) is not None:
            return ResourceID(_id)

    @property
    def last_pin_timestamp(self) -> datetime.datetime | None:
        """A `datetime.datetime` object representing when the last pinned message in this channel was pinned."""
        if (_datetime_formatted := self._data.get("last_pin_timestamp")) is not None:
            return datetime.datetime.fromisoformat(self._data["last_pin_timestamp"])


    @property
    def message_count(self) -> int | None:
        """The number of messages in this thread."""
        return self._data.get("message_count")

    @property
    def member_count(self) -> int | None:
        """The number of unique members in this thread, automatically stops counting at 50."""
        return self._data.get("member_count")

    @property
    def thread_metadata(self) -> ThreadMetadata | None:
        """Extra Thread Metadata."""
        if (_metadata := self._data.get("thread_metadata")) is not None:
            return ThreadMetadata(_metadata)

    @property
    def default_auto_archive_duration(self) -> int | None:
        """The default auto archive duration of this channel. Copied onto newly created threads."""
        return self._data.get("default_auto_archive_duration")

    @property
    def permissions(self) -> Permissions | None:
        """The permissions for this channel."""
        if (_perms := self._data.get("permissions")) is not None:
            return Permissions(_perms)._permissionize()

    @property
    def total_messages_all_time(self) -> int | None:
        """The total messages ever sent in this channel. Doesn't decrement whenever a message is deleted, like the `total_messages` field does."""
        return self._data.get("total_message_sent")

    # other fields are non-implemented objects

    @property
    def applied_tags(self) -> list[ResourceID] | None:
        """All applied tags to this channel."""
        return [ResourceID(id) for id in self._data["applied_tags"]] if self._data.get("applied_tags") else None

    @property
    def default_thread_ratelimit(self) -> int | None:
        """The default ratelimit to put on new created threads in a channel."""
        return self._data.get("default_thread_rate_limit_per_user")

    @property
    def default_sort_order(self) -> int | None:
        """The default sort order type used to order posts inside thread and media channels."""
        return self._data.get("default_sort_order")

    @property
    def default_forum_layout(self) -> int | None:
        """The default forum layout type used to display posts in forum channels."""
        return self._data.get("default_forum_layout")


class DMChannel(Channel):
    """An object that represents a channel in the context of a DM. Inherits from `inkcord.Channel`."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.recipients: "list[User] | User | None" = None
        """The recipients of this Group DM, if applicable."""
        self.icon: str | None = (
            f"https://cdn.discordapp.com/{data["icon"]}.png"
            if data.get("icon")
            else None
        )
        """The icon hash of this Group DM, if applicable."""
        self.owner_id = ResourceID(data["owner_id"]) if data.get("owner_id") else None
        """The id of the owner of the Group DM, if applicable."""
        self.application_id = (
            ResourceID(data["application_id"]) if data.get("application_id") else None
        )
        """The id of the app that made this DM, if applicable."""
        self.managed: bool = (
            data["managed"] if data.get("managed") else None
        )  # pyright: ignore[reportAttributeAccessIssue]
        """Whether this Group DM is managed by an application, if applicable."""


class VoiceChannel(Channel):
    """An object that represents a channel in the context of a call, or a voice channel in a Guild. Inherits from `inkcord.Channel`."""

    def __init__(self, data: dict):
        super().__init__(data)
        self.bitrate: int = data["bitrate"]
        """The bitrate of this voice channel (in bits)"""
        self.user_limit: int = data["user_limit"]
        """The number of users that can be in this voice channel at once."""
        self.rtc_region = (
            ResourceID(data["rtc_region"]) if data.get("rtc_region") else None
        )
        """The voice region ID for the voice channel. May be None."""
        self.video_quality_mode: int = self._data["video_quality_mode"]
        """The video quality mode for this channel. 0 means it's automatically chosen to protect performance, and 1 means 720p."""

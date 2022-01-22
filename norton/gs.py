from datetime import datetime, time
from operator import pos, truediv
from typing import final
import nextcord
from nextcord import Embed
from nextcord.ext import commands, menus
from nextcord import client
from nextcord import activity
from nextcord.utils import get
import io 
from googlesearch import search 
from datetime import datetime, timedelta, timezone
from nextcord import role
from nextcord import message
from nextcord.embeds import E
from nextcord.ext import commands
from random import randint
import aiofiles
import asyncio
import re
import math
from nextcord.interactions import Interaction
import asyncio
import functools
import itertools
import math
import random
import nextcord
import os
from nextcord.ext import commands
from nextcord.utils import get
from nextcord import FFmpegPCMAudio
from nextcord import TextChannel
import nextcord
from async_timeout import timeout
import datetime as dt
from nextcord.ext import commands
import os 
import nextcord
from nextcord.ext import commands
from nextcord.ext import commands
import nextcord
import pytz
import asyncio
import youtube_dl
import logging
import math
from urllib import request
from nextcord.ext import commands
import nextcord
import asyncio
import youtube_dl
import logging
import math
from urllib import request
from async_timeout import timeout
from nextcord import FFmpegPCMAudio
from nextcord import TextChannel
from youtube_dl import YoutubeDL
from nextcord.ext import commands, tasks
from nextcord.voice_client import VoiceClient
from random import choice
from io import BytesIO
import aiohttp
from nextcord.ui import view 
from time import sleep
from difflib import get_close_matches
from typing import List
import asyncio
import functools
import itertools
import math
import random
import youtube_dl
from async_timeout import timeout

intents = nextcord.Intents.default()
intents.members = True
intents.presences = True



class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.persistent_views_added = False

    async def on_ready(self):
        async with aiofiles.open("reaction_roles.txt", mode="a") as temp:
            pass
        async with aiofiles.open("reaction_roles.txt", mode="r") as file:
            lines = await file.readlines()
            for line in lines:
                data = line.split(" ")
                client.reaction_roles.append((int(data[0]), int(data[1]), data[2].strip("\n")))
        if not self.persistent_views_added:
            self.add_view(Close())
            self.add_view(TTP1())
            self.add_view(TTP3())
            self.add_view(Tickett())
            self.add_view(Panel4())
            self.add_view(Panel5())
		
            self.persistent_views_added = True

        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


client = Bot(command_prefix = commands.when_mentioned_or('>'), intents=intents)
client.reaction_roles = []
client.ticket_configs = {}
client.remove_command('help')



class TicTacToeButton(nextcord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int):
        # A label is required, but we don't need one so a zero-width space is used
        # The row parameter tells the View which row to place the button under.
        # A View can only contain up to 5 rows -- each row can only have 5 buttons.
        # Since a Tic Tac Toe grid is 3x3 that means we have 3 rows and 3 columns.
        super().__init__(style=nextcord.ButtonStyle.secondary, label='\u200b', row=y)
        self.x = x
        self.y = y

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: nextcord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.x]
        if state in (view.X, view.O):
            return

        if view.current_player == view.X:
            self.style = nextcord.ButtonStyle.danger
            self.label = 'X'
            self.disabled = True
            view.board[self.y][self.x] = view.X
            view.current_player = view.O
            content = "It is now O's turn"
        else:
            self.style = nextcord.ButtonStyle.success
            self.label = 'O'
            self.disabled = True
            view.board[self.y][self.x] = view.O
            view.current_player = view.X
            content = "It is now X's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.X:
                content = 'X won!'
            elif winner == view.O:
                content = 'O won!'
            else:
                content = "It's a tie!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


# This is our actual board View
class TicTacToe(nextcord.ui.View):
    # This tells the IDE or linter that all our children will be TicTacToeButtons
    # This is not required
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # Our board is made up of 3 by 3 TicTacToeButtons
        # The TicTacToeButton maintains the callbacks and helps steer
        # the actual game.
        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y))

    # This method checks for the board winner -- it is used by the TicTacToeButton
    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check vertical
        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        # Check diagonals
        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        # If we're here, we need to check if a tie was made
        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None





# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''


class VoiceError(Exception):
    pass


class YTDLError(Exception):
    pass


class YTDLSource(nextcord.PCMVolumeTransformer):
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }

    ytdl = youtube_dl.YoutubeDL(YTDL_OPTIONS)

    def __init__(self, ctx: commands.Context, source: nextcord.FFmpegPCMAudio, *, data: dict, volume: float = 0.5):
        super().__init__(source, volume)

        self.requester = ctx.author
        self.channel = ctx.channel
        self.data = data

        self.uploader = data.get('uploader')
        self.uploader_url = data.get('uploader_url')
        date = data.get('upload_date')
        self.upload_date = date[6:8] + '.' + date[4:6] + '.' + date[0:4]
        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.tags = data.get('tags')
        self.url = data.get('webpage_url')
        self.views = data.get('view_count')
        self.likes = data.get('like_count')
        self.dislikes = data.get('dislike_count')
        self.stream_url = data.get('url')

    def __str__(self):
        return '**{0.title}** by **{0.uploader}**'.format(self)

    @classmethod
    async def create_source(cls, ctx: commands.Context, search: str, *, loop: asyncio.BaseEventLoop = None):
        loop = loop or asyncio.get_event_loop()

        partial = functools.partial(cls.ytdl.extract_info, search, download=False, process=False)
        data = await loop.run_in_executor(None, partial)

        if data is None:
            raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        if 'entries' not in data:
            process_info = data
        else:
            process_info = None
            for entry in data['entries']:
                if entry:
                    process_info = entry
                    break

            if process_info is None:
                raise YTDLError('Couldn\'t find anything that matches `{}`'.format(search))

        webpage_url = process_info['webpage_url']
        partial = functools.partial(cls.ytdl.extract_info, webpage_url, download=False)
        processed_info = await loop.run_in_executor(None, partial)

        if processed_info is None:
            raise YTDLError('Couldn\'t fetch `{}`'.format(webpage_url))

        if 'entries' not in processed_info:
            info = processed_info
        else:
            info = None
            while info is None:
                try:
                    info = processed_info['entries'].pop(0)
                except IndexError:
                    raise YTDLError('Couldn\'t retrieve any matches for `{}`'.format(webpage_url))

        return cls(ctx, nextcord.FFmpegPCMAudio(info['url'], **cls.FFMPEG_OPTIONS), data=info)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} seconds'.format(seconds))

        return ', '.join(duration)


class Song:
    __slots__ = ('source', 'requester')

    def __init__(self, source: YTDLSource):
        self.source = source
        self.requester = source.requester

    def create_embed(self):
        embed = (nextcord.Embed(title='Now playing',
                               description='```css\n{0.source.title}\n```'.format(self),
                               color=nextcord.Color.blurple())
                 .add_field(name='Duration', value=self.source.duration)
                 .add_field(name='Requested by', value=self.requester.mention)
                 .add_field(name='Uploader', value='[{0.source.uploader}]({0.source.uploader_url})'.format(self))
                 .add_field(name='URL', value='[Click]({0.source.url})'.format(self))
                 .set_thumbnail(url=self.source.thumbnail))

        return embed


class SongQueue(asyncio.Queue):
    def __getitem__(self, item):
        if isinstance(item, slice):
            return list(itertools.islice(self._queue, item.start, item.stop, item.step))
        else:
            return self._queue[item]

    def __iter__(self):
        return self._queue.__iter__()

    def __len__(self):
        return self.qsize()

    def clear(self):
        self._queue.clear()

    def shuffle(self):
        random.shuffle(self._queue)

    def remove(self, index: int):
        del self._queue[index]


class VoiceState:
    def __init__(self, client, ctx):
        self.client = client
        self._ctx = ctx

        self.current = None
        self.voice = None
        self.next = asyncio.Event()
        self.songs = SongQueue()

        self._loop = False
        self._volume = 0.5
        self.skip_votes = set()

        self.audio_player = client.loop.create_task(self.audio_player_task())

    def __del__(self):
        self.audio_player.cancel()

    @property
    def loop(self):
        return self._loop

    @loop.setter
    def loop(self, value: bool):
        self._loop = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: float):
        self._volume = value

    @property
    def is_playing(self):
        return self.voice and self.current

    async def audio_player_task(self):
        while True:
            self.next.clear()

            if not self.loop:
                # Try to get the next song within 3 minutes.
                # If no song will be added to the queue in time,
                # the player will disconnect due to performance
                # reasons.
                try:
                    async with timeout(180):  # 3 minutes
                        self.current = await self.songs.get()
                except asyncio.TimeoutError:
                    self.client.loop.create_task(self.stop())
                    return

            self.current.source.volume = self._volume
            self.voice.play(self.current.source, after=self.play_next_song)
            await self.current.source.channel.send(embed=self.current.create_embed())

            await self.next.wait()

    def play_next_song(self, error=None):
        if error:
            raise VoiceError(str(error))

        self.next.set()

    def skip(self):
        self.skip_votes.clear()

        if self.is_playing:
            self.voice.stop()

    async def stop(self):
        self.songs.clear()

        if self.voice:
            await self.voice.disconnect()
            self.voice = None


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.voice_states = {}

    def get_voice_state(self, ctx: commands.Context):
        state = self.voice_states.get(ctx.guild.id)
        if not state:
            state = VoiceState(self.client, ctx)
            self.voice_states[ctx.guild.id] = state

        return state

    def cog_unload(self):
        for state in self.voice_states.values():
            self.client.loop.create_task(state.stop())

    def cog_check(self, ctx: commands.Context):
        if not ctx.guild:
            raise commands.NoPrivateMessage('This command can\'t be used in DM channels.')

        return True

    async def cog_before_invoke(self, ctx: commands.Context):
        ctx.voice_state = self.get_voice_state(ctx)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('An error occurred: {}'.format(str(error)))

    @commands.command(name='join', invoke_without_subcommand=True)
    async def _join(self, ctx: commands.Context):
        """Joins a voice channel."""

        destination = ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()
        await ctx.send("Successfully joined the voice channel!")

    @commands.command(name='summon')
    async def _summon(self, ctx: commands.Context, *, channel: nextcord.VoiceChannel = None):
        """Summons the client to a voice channel.
        If no channel was specified, it joins your channel.
        """

        if not channel and not ctx.author.voice:
            raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

        destination = channel or ctx.author.voice.channel
        if ctx.voice_state.voice:
            await ctx.voice_state.voice.move_to(destination)
            return

        ctx.voice_state.voice = await destination.connect()
        await ctx.send("Successfully joined the voice channel!")

    @commands.command(name='leave', aliases=['disconnect'])
    async def _leave(self, ctx: commands.Context):
        """Clears the queue and leaves the voice channel."""

        if not ctx.voice_state.voice:
            return await ctx.send('Not connected to any voice channel.')

        await ctx.voice_state.stop()
        del self.voice_states[ctx.guild.id]
        await ctx.send("Successfully disconnected the voice channel!")

    @commands.command(name='volume')
    async def _volume(self, ctx: commands.Context, *, volume: int):
        """Sets the volume of the player."""

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        if 0 > volume > 100:
            return await ctx.send('Volume must be between 0 and 100')

        ctx.voice_state.volume = volume / 100
        await ctx.send('Volume of the player set to {}%'.format(volume))

    @commands.command(name='now', aliases=['current', 'playing'])
    async def _now(self, ctx: commands.Context):
        """Displays the currently playing song."""

        await ctx.send(embed=ctx.voice_state.current.create_embed())

    @commands.command(name='pause')
    async def _pause(self, ctx: commands.Context):
        """Pauses the currently playing song."""

        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_playing():
            ctx.voice_state.voice.pause()
            await ctx.message.add_reaction('⏯')
            await ctx.send("Successfully paused the song!")

    @commands.command(name='resume')
    async def _resume(self, ctx: commands.Context):
        """Resumes a currently paused song."""

        if ctx.voice_state.is_playing and ctx.voice_state.voice.is_paused():
            ctx.voice_state.voice.resume()
            await ctx.message.add_reaction('⏯')
            await ctx.send("Successfully resumed the song!")

    @commands.command(name='stop')
    async def _stop(self, ctx: commands.Context):
        """Stops playing song and clears the queue."""

        ctx.voice_state.songs.clear()

        if ctx.voice_state.is_playing:
            ctx.voice_state.voice.stop()
            await ctx.message.add_reaction('⏹')
            await ctx.send("Successfully stopped the song!")

    @commands.command(name='skip')
    async def _skip(self, ctx: commands.Context):
        """Vote to skip a song. The requester can automatically skip.
        3 skip votes are needed for the song to be skipped.
        """
        if not ctx.voice_state.is_playing:
            return await ctx.send('Not playing any music right now...')
        channel = client.get_channel(864103846494470154)
        channel2 = client.get_channel(882287663875502152)
        members = channel.members
        if len(members) <3:
            await ctx.message.add_reaction('⏭')
            await ctx.send("Successfully skipped the song!")
            ctx.voice_state.skip()
        members2 = channel2.members
        if len(members2) <3:
            await ctx.message.add_reaction('⏭')
            await ctx.send("Successfully skipped the song!")
            ctx.voice_state.skip()



        voter = ctx.message.author
        if voter == ctx.voice_state.current.requester:
            await ctx.message.add_reaction('⏭')
            ctx.voice_state.skip()

        elif voter.id not in ctx.voice_state.skip_votes:
            ctx.voice_state.skip_votes.add(voter.id)
            total_votes = len(ctx.voice_state.skip_votes)

            if total_votes >= 3:
                await ctx.message.add_reaction('⏭')
                await ctx.send("Successfully skipped the song!")
                ctx.voice_state.skip()
            else:
                await ctx.send('Skip vote added, currently at **{}/3**'.format(total_votes))

        else:
            await ctx.send('You have already voted to skip this song.')

    @commands.command(name="forceskip")
    @commands.has_permissions(administrator=True)
    async def _forceskip(self, ctx:commands.Context):

        if not ctx.voice_state.is_playing:
            return await ctx.send('Not playing any music right now...')

        await ctx.message.add_reaction('⏭')
        await ctx.send("Successfully skipped the song!")
        ctx.voice_state.skip()


    @commands.command(name='queue')
    async def _queue(self, ctx: commands.Context, *, page: int = 1):
        """Shows the player's queue.
        You can optionally specify the page to show. Each page contains 10 elements.
        """

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        items_per_page = 10
        pages = math.ceil(len(ctx.voice_state.songs) / items_per_page)

        start = (page - 1) * items_per_page
        end = start + items_per_page

        queue = ''
        for i, song in enumerate(ctx.voice_state.songs[start:end], start=start):
            queue += '`{0}.` [**{1.source.title}**]({1.source.url})\n'.format(i + 1, song)

        embed = (nextcord.Embed(description='**{} tracks:**\n\n{}'.format(len(ctx.voice_state.songs), queue))
                 .set_footer(text='Viewing page {}/{}'.format(page, pages)))
        await ctx.send(embed=embed)

    @commands.command(name='shuffle')
    async def _shuffle(self, ctx: commands.Context):
        """Shuffles the queue."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.shuffle()
        await ctx.message.add_reaction('✅')
        await ctx.send("Successfully shuffled the queue!")

    @commands.command(name='remove')
    async def _remove(self, ctx: commands.Context, index: int):
        """Removes a song from the queue at a given index."""

        if len(ctx.voice_state.songs) == 0:
            return await ctx.send('Empty queue.')

        ctx.voice_state.songs.remove(index - 1)
        await ctx.message.add_reaction('✅')
        await ctx.send("Successfully removed the song from the queue")

    @commands.command(name='loop')
    async def _loop(self, ctx: commands.Context):
        """Loops the currently playing song.
        Invoke this command again to unloop the song.
        """

        if not ctx.voice_state.is_playing:
            return await ctx.send('Nothing being played at the moment.')

        # Inverse boolean value to loop and unloop.
        ctx.voice_state.loop = not ctx.voice_state.loop
        await ctx.message.add_reaction('✅')
        await ctx.send("Successfully looped the song!")

    @commands.command(name='play')
    async def _play(self, ctx: commands.Context, *, search: str):
        """Plays a song.
        If there are songs in the queue, this will be queued until the
        other songs finished playing.
        This command automatically searches from various sites if no URL is provided.
        A list of these sites can be found here: https://rg3.github.io/youtube-dl/supportedsites.html
        """

        if not ctx.voice_state.voice:
            await ctx.invoke(self._join)

        async with ctx.typing():
            try:
                source = await YTDLSource.create_source(ctx, search, loop=self.client.loop)
            except YTDLError as e:
                embed=nextcord.Embed(description='An error occurred while processing this request: {}'.format(str(e)))
                await ctx.send(embed=embed)
            else:
                song = Song(source)

                await ctx.voice_state.songs.put(song)
                embed=nextcord.Embed(description='Enqueued {}'.format(str(source)))
                await ctx.send(embed=embed)

    @_join.before_invoke
    @_play.before_invoke
    async def ensure_voice_state(self, ctx: commands.Context):
        if not ctx.author.voice or not ctx.author.voice.channel:
            raise commands.CommandError('You are not connected to any voice channel.')

        if ctx.voice_client:
            if ctx.voice_client.channel != ctx.author.voice.channel:
                raise commands.CommandError('Bot is already in a voice channel.')
client.add_cog(Music(client))



for ext in ('fungs','gsmodmail' ):
    client.load_extension(f'{ext}')

async def ch_pr():
    await client.wait_until_ready()
    statuses = ["to >help", "DM to Contact Staff","OFFICIAL BOT OF GRAPHICS STUDIO"]
    
    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity=nextcord.Game(name=status))

        await asyncio.sleep(5)
client.loop.create_task(ch_pr())


@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):

        embed = nextcord.Embed(description="<a:caution:917722875459436544> You are Missing Permissions to do!", colour=0x5AFFBB)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


    elif isinstance(error,commands.MissingRequiredArgument):
        embed = nextcord.Embed(description="<a:caution:917722875459436544> Please enter all the required arguments!", colour=0x5AFFBB)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()

    elif isinstance(error, commands.BadArgument):
        embed = nextcord.Embed(description=" <a:caution:917722875459436544> Incorrect Arguments given!", colour=0x5AFFBB)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()

    elif isinstance(error, commands.DisabledCommand):
        embed= nextcord.Embed(description=" <a:caution:917722875459436544> The command is disabled, please enable it via `>toggle <command>`", colour=0x5AFFBB)
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


    elif isinstance(error, commands.CommandNotFound):
        cmd = ctx.invoked_with
        cmds = [cmd.name for cmd in client.commands]
        matches = get_close_matches(cmd, cmds)
        if len(matches) > 0:
            embed = nextcord.Embed(description = f' <a:caution:917722875459436544> Command "{cmd}" not found, maybe you meant "{matches[0]}"?', colour=0x5AFFBB)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()
        else:
            embed = nextcord.Embed(description=f' <a:caution:917722875459436544> Command "{cmd}" not found!', colour=0x5AFFBB)
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()

    else:
        raise error

@client.command()
async def toggle(ctx,*,command):
    command = client.get_command(command)
    if command == None:
        await ctx.send(f"{command} was not found, or you forgot to provide one!")
    elif ctx.command == command:
        await ctx.send(f"{command} cannot be disabled!")
    else:
        command.enabled = not command.enabled
        ternary = "enabled" if command.enabled else "disabled"
        await ctx.send(f"Command {command.qualified_name} has been {ternary}")
    
@client.command(aliases=["addrole"])
@commands.has_permissions(manage_roles=True)
async def addroles(ctx, role:nextcord.Role, user: nextcord.Member):
    await user.add_roles(role)
    await ctx.send(f"Given {role.mention} to {user.mention}")

@client.command(aliases=["delrole"])
@commands.has_permissions(manage_roles=True)
async def removeroles(ctx, role:nextcord.Role, user: nextcord.Member):
    await user.remove_roles(role)
    await ctx.send(f"Removed {role.mention} from {user.mention}")






class Dropdown(nextcord.ui.Select):
    def __init__(self):
        selectOptions = {
            nextcord.SelectOption(label = "Admin Commands", description="Kick,Ban,Mute etc.", emoji='📳'),
            nextcord.SelectOption(label = "Commands For Users", description="Avatar, Whois, DM", emoji='👥'),
            nextcord.SelectOption(label="Music", description="Music Commands", emoji="🎧"),
            nextcord.SelectOption(label = "Home", description="Go back to the original help page", emoji='🏡')
        }
        super().__init__(placeholder="Select Help options", min_values = 1, max_values=1, options=selectOptions )
    
    async def callback(self, interaction: nextcord.Interaction):
        if self.values[0] == "Admin Commands":
            
            curr_time = dt.datetime.now()
            dtm = curr_time.strftime("%dth/%B/%Y")
            embed = nextcord.Embed(description="""𝙰𝚍𝚖𝚒𝚗 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜
> 「<a:starwhite:917723116078264330>」 **Reject** - Rejects a member
> 「<a:starwhite:917723116078264330>」  **Accept** - Accepts a user
> 「<a:starwhite:917723116078264330>」 **Kick**- This will kick a member from the server
> 「<a:starwhite:917723116078264330>」 **Hardmute** - hardmutes member by removing the roles
> 「<a:starwhite:917723116078264330>」 **Ban**- This will Ban a member from the Server
> 「<a:starwhite:917723116078264330>」 **Unban**:- This will Ban an Unbanned Member from the server
> 「<a:starwhite:917723116078264330>」 **Mute**- This will mute a member indefinitely
> 「<a:starwhite:917723116078264330>」**Unmute**- This will unmute a muted member from the server
> 「<a:starwhite:917723116078264330>」 **Clear** - This will clear a definite number of messages
> 「<a:starwhite:917723116078264330>」 **Toggle** - Either disables a command or enables a disabled command
> 「<a:starwhite:917723116078264330>」 **Slowmode** - Sets the slowmode of a channel
> 「<a:starwhite:917723116078264330>」 **Addroles** - Adds a role to a user
> 「<a:starwhite:917723116078264330>」 **Removeroles** - Removes a role from a user
> 「<a:starwhite:917723116078264330>」 **Unlock** - Unlocks a lock channel
> 「<a:starwhite:917723116078264330>」 **Tempmute** - Tempmutes a member
> 「<a:starwhite:917723116078264330>」 **Inrole** - Shows the member of people in a role
> 「<a:starwhite:917723116078264330>」 **Steal** - Steals an emoji from another server
> 「<a:starwhite:917723116078264330>」 **Reaction Roles** - Used to set-up reaction roles
> 「<a:starwhite:917723116078264330>」 **Echo** - Echoes something
> 「<a:starwhite:917723116078264330>」  **Embed** - Echo in embed form
> 「<a:starwhite:917723116078264330>」 **Delcateg** - Deletes a category and its channels
> 「<a:starwhite:917723116078264330>」  **DM** - DM's a user with the given ID and message""", color=0x5AFFBB)
            embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
            embed.set_footer(text="Generated by Graphics Studio")
            embed.timestamp = dt.datetime.now()
    		
            

            return await interaction.message.edit(embed=embed)
        if self.values[0] == "Commands For Users":
            curr_time = dt.datetime.now()
            dtm = curr_time.strftime("%dth/%B/%Y")
            embed = nextcord.Embed(description="""𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜
> 「<a:starpink:917723124903079947>」 **AV** - Displays the avatar of a member
> 「<a:starpink:917723124903079947>」**Whois** - Displays about the member
> 「<a:starpink:917723124903079947>」**Snipe** - Shows the Last deleted message in that channel
> 「<a:starpink:917723124903079947>」**Tic** - Starts a tic-tac-toe game either yourself or someone else
> 「<a:starpink:917723124903079947>」**Meme** - Self-Explanatory
> 「<a:starpink:917723124903079947>」**NC** - Shows the number of commands in the bot
> 「<a:starpink:917723124903079947>」**Find** - Searches for something in Google and displays the First Result
 """, color=0x5AFFBB)
            embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
            embed.set_footer(text="Generated by Graphics Studio")
            embed.timestamp = dt.datetime.now()
    		
            
            return await interaction.message.edit(embed=embed)
        if self.values[0] == "Music":
            curr_time = dt.datetime.now()
            dtm = curr_time.strftime("%dth/%B/%Y")
            embed=nextcord.Embed(description="""𝙼𝚞𝚜𝚒𝚌 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜

> 「<a:starblue:917723136747769857>」Summon - Summons the bot to a voice channel
> 「<a:starblue:917723136747769857>」Forceskip - Force-skips a song
> 「<a:starblue:917723136747769857>」Shuffle - Shuffles the queue
> 「<a:starblue:917723136747769857>」Queue - Shows the music queue
> 「<a:starblue:917723136747769857>」Loop - Loops a song
> 「<a:starblue:917723136747769857>」Join - Joins a voice channel
> 「<a:starblue:917723136747769857>」Play - Starts playing a song
> 「<a:starblue:917723136747769857>」Volume - Adjusts the volume of the player
> 「<a:starblue:917723136747769857>」Leave - Leaves the voice channel
> 「<a:starblue:917723136747769857>」Pause - Pauses a song
> 「<a:starblue:917723136747769857>」Resume - Resumes the song
> 「<a:starblue:917723136747769857>」Skip - Skips a song
> 「<a:starblue:917723136747769857>」Remove - Removes an item number from the queue
> 「<a:starblue:917723136747769857>」Now - Shows the song which is currently playing""")
            
            embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
            embed.set_footer(text="Generated by Graphics Studio")
            embed.timestamp = dt.datetime.now()
            return await interaction.message.edit(embed=embed)
        if self.values[0] == "Home":
            embed=nextcord.Embed(description="""𝙶𝚛𝚊𝚙𝚑𝚒𝚌𝚜 𝚂𝚝𝚞𝚍𝚒𝚘 ™

𝒲ℯ 𝒶𝓇ℯ 𝒶𝓃 𝓊𝓅𝒸ℴ𝓂𝒾𝓃ℊ 𝒸ℴ𝓂𝓂𝓊𝓃𝒾𝓉𝓎 ℴ𝒻 𝒢𝓇𝒶𝓅𝒽𝒾𝒸𝓈 𝒟ℯ𝓈𝒾ℊ𝓃ℯ𝓇𝓈 , 𝒲ℯ ℴ𝒻𝒻ℯ𝓇 𝓆𝓊𝒶𝓁𝒾𝓉𝓎 𝓅𝓇ℴ𝒹𝓊𝒸𝓉𝓈 𝒶𝓉 𝒸𝒽ℯ𝒶𝓅 𝓅𝓇𝒾𝒸ℯ𝓈!

> <a:starwhite:917723116078264330> 𝙵𝚘𝚛 𝚋𝚘𝚝 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 , 𝚞𝚜𝚎 𝚍𝚛𝚘𝚙 𝚍𝚘𝚠𝚗 𝚖𝚎𝚗𝚞""", colour =0x5AFFBB)
            embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
            embed.set_footer(text="Generated by Graphics Studio")
            embed.timestamp = dt.datetime.now()
            return await interaction.message.edit(embed=embed)
            

class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())



@client.group(invoke_without_command = True)
async def help(ctx):
    curr_time = dt.datetime.now()
    dtm = curr_time.strftime("%dth/%B/%Y")
    view = DropdownView()
    embed=nextcord.Embed(description="""𝙶𝚛𝚊𝚙𝚑𝚒𝚌𝚜 𝚂𝚝𝚞𝚍𝚒𝚘 ™

𝒲ℯ 𝒶𝓇ℯ 𝒶𝓃 𝓊𝓅𝒸ℴ𝓂𝒾𝓃ℊ 𝒸ℴ𝓂𝓂𝓊𝓃𝒾𝓉𝓎 ℴ𝒻 𝒢𝓇𝒶𝓅𝒽𝒾𝒸𝓈 𝒟ℯ𝓈𝒾ℊ𝓃ℯ𝓇𝓈 , 𝒲ℯ ℴ𝒻𝒻ℯ𝓇 𝓆𝓊𝒶𝓁𝒾𝓉𝓎 𝓅𝓇ℴ𝒹𝓊𝒸𝓉𝓈 𝒶𝓉 𝒸𝒽ℯ𝒶𝓅 𝓅𝓇𝒾𝒸ℯ𝓈!

> <a:starwhite:917723116078264330> 𝙵𝚘𝚛 𝚋𝚘𝚝 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 , 𝚞𝚜𝚎 𝚍𝚛𝚘𝚙 𝚍𝚘𝚠𝚗 𝚖𝚎𝚗𝚞""", colour =0x5AFFBB)
    embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
    embed.set_footer(text="Generated by Graphics Studio")
    embed.timestamp = dt.datetime.now()
    await ctx.send(embed=embed, view=view)

@help.command()
@commands.has_permissions(administrator=True)
async def kick(ctx):
    em = nextcord.Embed(title = "KICK", description = "Kicks a member from the server" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">kick <member> <reason>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def warn(ctx):
    em = nextcord.Embed(title = "WARN", description = "Warns a member in the server" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">warn <member> <reason>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def warns(ctx):
    em = nextcord.Embed(title = "WARNS", description = "Shows the number of warns a user has" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">warns <member>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def set_reaction(ctx):
    em = nextcord.Embed(title = "Reaction Roles", description = "Adds the designated emoji the user mentions and the role too" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">set_reaction <ping the role you are setting reaction roles for> <message ID> <emoji>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def removeroles(ctx):
    em = nextcord.Embed(title = "REMOVE ROLES", description = "Removes a role from a member (aliases = delrole)" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">removeroles <role> <user>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def addroles(ctx):
    em = nextcord.Embed(title = "ADD ROLES", description = "Adds a role to a member (aliases = addrole) " , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">addroles <role> <user>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def ban(ctx):
    em = nextcord.Embed(title = "BAN", description = "Bans a member from the server" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">ban <member> <reason>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def unban(ctx):
    em = nextcord.Embed(title = "UNBAN", description = "Unbans a member from the server" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">unban <member>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def mute(ctx):
    em = nextcord.Embed(title = "MUTE", description = "Mute a member from the server" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">mute <member> <reason>")

    await ctx.send(embed = em)

@help.command()
async def whois(ctx):
    em = nextcord.Embed(title = "WHOIS", description = "Shows about the member" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">whois <member>")

    await ctx.send(embed = em)

@help.command()
async def av(ctx):
    em = nextcord.Embed(title = "AV", description = "Shows a member's avatar" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">av <member>")

    await ctx.send(embed = em)

@help.command()
async def snipe(ctx):
    em = nextcord.Embed(title = "SNIPE", description = "Shows the last deleted message from any channel in the server including the channel this command is used in" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">snipe")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    em = nextcord.Embed(title = "TICKET", description = "The bot reacts with a ticket symbol, if any other user reacts upon it a ticket would be created" , colour = 0x5AFFBB)

    em.add_field(name = "*Syntax*", value  = ">configure_ticket <Message ID> <Category ID>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def dm(ctx):
    em = nextcord.Embed(title = "DM", description = "The bot DM's a given user" , colour = 0x5AFFBB)

    em.add_field(name = "**Syntax**", value  = ">dm <User ID> <message>")

    await ctx.send(embed = em)





@help.command()
@commands.has_permissions(administrator=True)
async def reaction(ctx):
    em = nextcord.Embed(title = "REACTION", description = "Sets a reaction in a message" , colour = 0x5AFFBB)

    em.add_field(name = "**Syntax**", value  = ">set_reaction <role> <message id > <emoji>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def echo(ctx):
    em = nextcord.Embed(title = "ECHO", description = "Echoes a message. The channel parameter is optional" , colour = 0x5AFFBB)

    em.add_field(name = "**Syntax**", value  = ">echo <channel> <message>")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def embed(ctx):
    em = nextcord.Embed(title = "EMBED", description = "Echoes a message in Embeded form" , colour = 0x5AFFBB)

    em.add_field(name = "**Syntax**", value  = "*embed ")

    await ctx.send(embed = em)



@help.command()
@commands.has_permissions(administrator=True)
async def slowmode(ctx):
    em = nextcord.Embed(title = "SLOWMODE", description = "Sets the slowmode for the channel this command is used in" , colour = 0x5AFFBB)

    em.add_field(name = "**Syntax**", value  = ">sm / !slowmode")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx):
    em = nextcord.Embed(title = "UNLOCK", description = "Unlocks the channel this command is used in" , colour = 0x5AFFBB)

    em.add_field(name = "**Syntax**", value  = ">unlock / >ul")

    await ctx.send(embed = em)

@help.command()
@commands.has_permissions(administrator=True)
async def lock(ctx):
    em = nextcord.Embed(title = "LOCK", description = "Locks the channel this command is used in" , colour = 0x5AFFBB)

    em.add_field(name = "**Syntax**", value  = ">lock / >l")

    await ctx.send(embed = em)





    

@client.command("clear")
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge( limit = amount)

@client.command("kick")
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : nextcord.Member,*,reason= "No reason provided"):
    if member.top_role >= ctx.author.top_role:
        embed=nextcord.Embed(description=" <a:caution:917722875459436544> You cant do that!")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        return
    try:
        await ctx.send(member.name + " has been kicked, For " + reason)
        embed=nextcord.Embed(f" You have been kicked from {ctx.guild.name}, For {reason}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
        await member.send(embed=embed)
    except:
        await ctx.send("The member has their DM's closed.")

    await member.kick(reason=reason)

@client.command("ban")
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : nextcord.Member,*,reason= "No reason provided"):
    if member.top_role >= ctx.author.top_role:
        embed=nextcord.Embed(description=" <a:caution:917722875459436544> You cant do that!")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        return
    try:
        await ctx.send(member.name + " has been banned , For " + reason)
        
        embed = nextcord.Embed(description=f" You have been banned from {ctx.guild.name}, For {reason}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
        await member.send(embed=embed)
    except:
        await ctx.send("The member has their DM's closed.")

    await member.ban(reason=reason)

@client.command("unban")
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')
    
    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name +" has been unbanned!")
            return
    
    await ctx.send(member+" was not found")

@client.command("hmute")
@commands.has_permissions(kick_members = True)
async def hardmute(ctx,member : nextcord.Member,*,reason= "None"):

    if member.top_role >= ctx.author.top_role:
        embed=nextcord.Embed(description=" <a:caution:917722875459436544> You cant do that!")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        return

    mutedRole =  ctx.guild.get_role(918103977181212732)
    roles = member.roles

    await member.edit(roles=[mutedRole])
    await member.add_roles(mutedRole, reason=reason)
    try:
        await ctx.send(f"{member.mention} has been muted in {ctx.guild.name} , For {reason}")
        embed=nextcord.Embed(description=f"You have been muted in {ctx.guild.name}, For {reason}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
        await member.send(embed=embed)
    except:
        await ctx.send("The member has their DM's closed.")

@client.command("mute")
@commands.has_permissions(kick_members = True)
async def mute(ctx,member : nextcord.Member,*,reason= "None"):

    if member.top_role >= ctx.author.top_role:
        embed=nextcord.Embed(description=f"<a:caution:917722875459436544> You cant do that!")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        return

    mutedRole =  ctx.guild.get_role(918103977181212732)

    await member.add_roles(mutedRole, reason=reason)
    try:
        await ctx.send(f"{member.mention} has been muted in {ctx.guild.name}, For {reason} ")
        embed = nextcord.Embed(description=f"You have been muted in {ctx.guild.name}, For {reason}")
        embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
        await member.send(embed=embed)
    except:
        await ctx.send("The member has their DM's closed.")



@client.command("unmute")
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member : nextcord.Member):

    if member.top_role >= ctx.author.top_role:
        embed=nextcord.Embed(description=" <a:caution:917722875459436544> You cant do that!")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        return

    mutedRole = ctx.guild.get_role(918103977181212732)

    if mutedRole not in member.roles:
        await ctx.send("The member is not muted!")

    else:

        await member.remove_roles(mutedRole)


        try:
            await ctx.send(member.mention + " has been unmuted")
            embed=nextcord.Embed(description=f"You have been unmuted from {ctx.guild.name}")
            embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
            await member.send(embed=embed)
        except:
            await ctx.send("The member has their DM's closed.")

@client.command(name="whois")
async def whois(ctx,user:nextcord.Member=None):

    if user==None:
        user=ctx.author

    rlist = []
    for role in user.roles:
      if role.name != "@everyone":
        rlist.append(role.mention)

    b = ", ".join(rlist)


    embed = nextcord.Embed(colour=user.color,timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar.url),
    embed.set_footer(text=f'Requested by - {ctx.author}', icon_url=ctx.author.avatar.url)

    embed.add_field(name='ID:',value=user.id,inline=False)
    embed.add_field(name='Name:',value=user.display_name,inline=False)

    embed.add_field(name='Created at:',value=user.created_at,inline=False)
    embed.add_field(name='Joined at:',value=f"{user.joined_at}",inline=False)
    x = ''.join([b])

    embed.add_field(name=f'Roles:({len(rlist)})',value=x,inline=False)
    embed.add_field(name='Top Role:',value=user.top_role.mention,inline=False)

    await ctx.send(embed=embed) 
    print("Worked")


@client.command("av")
async def av(ctx,user:nextcord.Member=None):

    if user==None:
        user=ctx.author

    embed = nextcord.Embed(title=f"{user}'s Avatar!", description = user.mention, color=0x5AFFBB, timestamp=ctx.message.created_at)
    embed.set_image(url=user.avatar.url)
    embed.set_footer(icon_url= ctx.author.avatar.url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)



snipe_message_content = None
snipe_message_author = None
snipe_message_id = None

@client.event
async def on_message_delete(message):

    global snipe_message_content
    global snipe_message_author
    global snipe_message_id

    snipe_message_content = message.content
    snipe_message_author = message.author.id
    snipe_message_id = message.id
    await asyncio.sleep(60)

    if message.id == snipe_message_id:
        snipe_message_author = None
        snipe_message_content = None
        snipe_message_id = None

@client.command()
async def snipe(message):
    if snipe_message_content==None:
        await message.channel.send("There's nothing to snipe.")
    else:
        embed = nextcord.Embed(title="Latest Sniped Message",description=f"Author of the message- <@!{snipe_message_author}>\nMessage Content - {snipe_message_content}")
        embed.set_footer(text=f"Requested {message.author.name}#{message.author.discriminator}", icon_url=message.author.avatar.url)
        await message.channel.send(embed=embed)
        return



@client.event
async def on_guild_join(guild):
    client.warnings[guild.id] = {}


@client.command()
@commands.has_permissions(manage_messages = True)
async def dm(ctx, member:nextcord.Member,*,args):
    try:
        embed=nextcord.Embed(description=f"{args}",colour=nextcord.Color.random())
        await member.send(embed=embed)
        await ctx.send(f"{args} sent to {member.name}#{member.discriminator}")
    except:
        return await ctx.send("The member has their DM'S off!")
        

 



      

    
@client.command()
@commands.has_permissions(manage_messages = True)
async def set_reaction(ctx, role: nextcord.Role=None, msg: nextcord.Message=None, emoji=None):
    if role != None and msg != None and emoji != None:
        await msg.add_reaction(emoji)
        client.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))
        
        async with aiofiles.open("reaction_roles.txt", mode="a") as file:
            emoji_utf = emoji.encode("utf-8")
            await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

        await ctx.channel.send("Reaction has been set.")
        
    else:
        await ctx.send("Invalid arguments.")

@client.event
async def on_raw_reaction_add(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            await payload.member.add_roles(client.get_guild(payload.guild_id).get_role(role_id))
            return

@client.event
async def on_raw_reaction_remove(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            guild = client.get_guild(payload.guild_id)
            await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
            return


@client.command()
@commands.has_permissions(manage_messages=True)
async def tempmute(ctx, member: nextcord.Member=None, time=None, *, reason=None):

    if member.top_role >= ctx.author.top_role:
        return await ctx.send("The member is either higher than you or same as the post of you in the role hierchy")

    if not member:
        await ctx.send("You must mention a member to mute!")
        return
    elif not time:
        await ctx.send("You must mention a time!")
        return
    else:
        if not reason:
            reason="No reason given"
        #Now timed mute manipulation
    try:
        time_interval = time[:-1] #Gets the numbers from the time argument, start to -1
        duration = time[-1] #Gets the timed manipulation, s, m, h, d
        if duration == "s":
            time_interval = time_interval * 1
        elif duration == "m":
            time_interval = time_interval * 60
        elif duration == "h":
            time_interval = time_interval * 60 * 60
        elif duration == "d":
            time_interval = time_interval * 86400
        else:
            await ctx.send("Invalid duration input")
            return
    except Exception as e:
        print(e)
        await ctx.send("Invalid time input")
        return
    guild = ctx.guild
    mutedRole = ctx.guild.get_role(890253433481867265)

    await member.edit(roles=[mutedRole])
    await member.add_roles(mutedRole, reason=reason)
    Muted_embed = nextcord.Embed(title="Muted a user", description=f"{member.mention} has muted by {ctx.author.mention} for {reason} to {time}", color=0x5AFFBB)
    Mute_embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
    await ctx.send(embed=Muted_embed)
    await member.send(embed=Muted_embed)
    await asyncio.sleep(int(time_interval))
    await member.remove_roles(mutedRole)
    unmute_embed = nextcord.Embed(title='Mute over!', description=f"{ctx.author.mention} muted to {member.mention} for {reason} is over after {time}" , color=0x5AFFBB)
    await ctx.send(embed=unmute_embed)
    await member.send(embed=unmute_embed)









@client.command()
@commands.has_permissions(administrator=True)
async def echo(ctx, channel: nextcord.TextChannel=None,*,args):
    await channel.send(args)
    await ctx.message.delete()
    print(args)


class MyEmbedDescriptionPageSource(menus.ListPageSource):
    def __init__(self, data, r):
        super().__init__(data, per_page=20)
        self.r = r

    async def format_page(self, menu, names):

        embed = Embed(title=f"Members in role {self.r.name}", description="\n".join(names))

        embed.set_footer(text=f'Page {menu.current_page + 1}/{self.get_max_pages()}')
        return embed


@client.command()
@commands.has_permissions(administrator=True)
async def inrole(ctx, r_id:int):
    print(r_id)
    g=client.get_guild(883054783446011936)
    r = g.get_role(r_id)
    names = [f"{m.name}#{m.discriminator}" for m in r.members]

    pages = menus.ButtonMenuPages(
        source=MyEmbedDescriptionPageSource(names, r),
        disable_buttons_after=True,
    )
    await pages.start(ctx)







@client.command()
@commands.has_permissions(administrator=True)
async def embed(ctx, channel: nextcord.TextChannel):
    embed = nextcord.Embed()

    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author
    try:
        await ctx.send("What should be the embed colour in hex code?Write `None` to skip, the color would be red from default!")
        msg = await client.wait_for('message', check=check,  timeout=60)

        if msg.content.lower() == 'none':
            embed.color = nextcord.Color.red()
        else:
            try:
                embed.colour = await commands.ColourConverter().convert(ctx, msg.content)
            except:
                return await ctx.send("Invalid Hex Code Provided! Please re-do the command!")
        await ctx.send("Please enter title!")
        msg = await client.wait_for('message',check = check,timeout= 60)
        embed.title = msg.content
        await ctx.send("Please enter description!")
        msg = await client.wait_for('message',check = check, timeout = 60)
        embed.description = msg.content
        await ctx.send("Please enter the url or write `None` to skip!")
        msg = await client.wait_for( 'message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("Alright the embed wouldnt have an image!")
        else:

            embed.set_image(url=msg.content)
        await ctx.send("Alright! Now enter the thumbnail's url or write `None` to skip!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("Alright there wouldn't be a thumbnail!")
        else:

            embed.set_thumbnail(url=msg.content)
        await ctx.send("Do you want the embed to have a footer?Write `None` to skip or `Yes` if you want it to have a footer!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("There wouldnt be a footer!")
            await channel.send(embed=embed)
        else:
            await ctx.send("Please enter the footer's icon url or write `None` to skip!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                await ctx.send("There wouldnt be an icon in the footer!")
            else:
                embed.set_footer(icon_url=msg.content)
            await ctx.send("Please enter the footer's Content!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                await ctx.send("Foooter content cant be `None`! Please use the `-embed` command again!")
                return

            else:
                embed.set_footer(text=msg.content)
                await channel.send(embed=embed)

        

    except asyncio.TimeoutError:
        await ctx.send("Timeout for responding!")
        return
    
   

    


@client.command(aliases=["sm"])
@commands.has_permissions(manage_messages=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    slowmode_embed = nextcord.Embed(title="Slowmode", description="A slowmode was set for this channel", color=0x5AFFBB)
    await ctx.send(embed=slowmode_embed, delete_after=5.0)

@client.command(aliases=["l"])
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : nextcord.TextChannel=None):
    guild = ctx.guild
    Community_Role = ctx.guild.get_role(918103978108133386)
    overwrite = ctx.channel.overwrites_for(Community_Role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(Community_Role, overwrite=overwrite)
    await ctx.send('Channel locked.')

@client.command(aliases=["ul"])
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : nextcord.TextChannel=None):
    guild=ctx.guild
    Community_Role = ctx.guild.get_role(918103978108133386)
    overwrite = ctx.channel.overwrites_for(Community_Role)
    overwrite.send_messages = True
    await ctx.channel.set_permissions(Community_Role, overwrite=overwrite)
    await ctx.send('Channel unlocked.')

@client.command()
async def steal(ctx, url:str,*,name):
    guild=ctx.guild
    async with aiohttp.ClientSession() as ses:
        async with ses.get(url) as r:
            try:
                imgOrGif = BytesIO(await r.read())
                bValue = imgOrGif.getvalue()
                if r.status in range(200,299):
                    emoji = await guild.create_custom_emoji(image = bValue, name=name)
                    await ctx.send("Emoji has been added")
                    await ses.close()
                else:
                    await ctx.send(f"This didnt work | {r.status}")
            except nextcord.HTTPException:
                await ctx.send("This file is too large!")







@help.command()
async def steal(ctx):
    embed=nextcord.Embed(title="STEAL", description="Steals an emoji from a server")
    embed.add_field(name="**SYNTAX**", value = ">steal <attachment url> <emoji name>")
    embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
    await ctx.send(embed=embed)


@client.command(aliases=["search"])
async def find(ctx,*, query):
    author = ctx.author.mention
    async with ctx.typing():
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            embed = nextcord.Embed(title=f"Here is the result of your search {author}", description=f"\n{j}")
        await ctx.send(embed=embed)
    



@client.event
async def on_message(message):


    if message.type == nextcord.MessageType.premium_guild_subscription:
        embed=nextcord.Embed(title="THANKS FOR BOOSTING | APPRECIATION", description=f"Thanks to {message.author.mention} for boosting our server")
        embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
        await message.channel.send(embed=embed)
    
    

    await client.process_commands(message)


@client.command(aliases=["rev"])
async def review(ctx,*,suggestion:str):
    embed=nextcord.Embed(title=f"Review by {ctx.author.name}#{ctx.author.discriminator}", description=f"{suggestion}")
    channel = nextcord.utils.get(ctx.guild.text_channels,name="💌〢𝚁𝚎𝚟𝚒𝚎𝚠｡ﾟ⊹" )
    await channel.send(embed=embed)






@client.command(
    aliases=["Tic", "tictactoe", "ttt","Tictactoe","TTT"]
)
async def tic(ctx):
    """Starts a tic-tac-toe game with yourself."""
    await ctx.send('Tic Tac Toe: X goes first', view=TicTacToe())

@client.command()
async def nc(ctx):
    a = (len(client.commands))
    print(a)
    await ctx.send(f"Number of commands is {a}")

@client.command()
async def delcateg(ctx, category: nextcord.CategoryChannel):
    delcategory = category # delcategory is our ID (category)
    channels = delcategory.channels # Get all channels of the category

    for channel in channels: # We search for all channels in a loop
        try:
            await channel.delete() # Delete all channels
        except AttributeError: # If the category does not exist/channels are gone
            pass
    await delcategory.delete()
    embed=nextcord.Embed(description="The Category And its channels were deleted",colour=0x5AFFBB)
    await ctx.send(embed=embed)# At the end we delete the category, if the loop is over

@client.command()
@commands.has_permissions(administrator=True)
async def accept(ctx, member:nextcord.Member):

    if member.top_role >= ctx.author.top_role:
        embed=nextcord.Embed(description=" <a:caution:917722875459436544> You cant do that!")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        return

    Role =  ctx.guild.get_role(918103988388380673)

    roles = ctx.guild.get_role(918103966108233808)


    await member.add_roles(Role)
    await member.add_roles(roles)


    embed=nextcord.Embed(description=f"{member.mention} has been accepted!")
    embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def reject(ctx, member:nextcord.Member):

    if member.top_role >= ctx.author.top_role:
        embed=nextcord.Embed(description=" <a:caution:917722875459436544> You cant do that!")
        msg = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
        return

    Role =  ctx.guild.get_role(918103988388380673)
    roles = ctx.guild.get_role(918103966108233808)

    await member.remove_roles(Role)
    await member.remove_roles(roles)


    embed=nextcord.Embed(description=f"{member.mention} has been rejected!")
    embed.set_image(url="https://cdn.discordapp.com/attachments/919626772713201715/929287134332993546/1641629594855.jpg")
    await ctx.send(embed=embed)

import chat_exporter
class TDownload(nextcord.ui.View):
    def __init__(self, turl):
        super().__init__(timeout=None)
        # we need to quote the query string to make a valid url. Discord will raise an error if it isn't valid.
        url = f'{turl}'

        # Link buttons cannot be made with the decorator
        # Therefore we have to manually create one.
        # We add the quoted url to the button, and add the button to the view.
        self.add_item(nextcord.ui.Button(label='Download Transcript', url=url))

@client.command()
@commands.has_permissions(administrator=True)
async def save(ctx, limit: int):
    tz_info = "Asia/Kolkata"
    transcript = await chat_exporter.export(ctx.channel, int(limit), tz_info, ctx.guild)

    if transcript is None:
        return

    transcript_file = nextcord.File(io.BytesIO(transcript.encode()),
                                    filename=f"transcript-{ctx.channel.name}.html")



    channel = nextcord.utils.get(ctx.guild.channels, id=918104098677604402)                               
    message = await channel.send(file=transcript_file)
    turl = message.attachments[0].url
    embed = nextcord.Embed(description=f"```TRANSCRIPT OF {ctx.channel.name}```\n\nThe Transcript file can be viewed by clicking on\n[This Link]({turl}) or from the button present belo, which will automatically download the transcript.html\nfile on your device and save you a few clicks or you can also download from the file above!")
    await channel.send(embed=embed)

class Close(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

    @nextcord.ui.button(label = "Transcript", style=nextcord.ButtonStyle.red, custom_id='transcript')
    async def tClose(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator is not True:
            await interaction.channel.send_message('You are missing perms to transcript the channel!',ephemeral=True)
        else:
            limit=10000
            tz_info = 'UTC'
            transcript = await chat_exporter.export(interaction.channel, interaction.guild, limit, tz_info)

            if transcript is None:
                return

            transcript_file = nextcord.File(io.BytesIO(transcript.encode()),
                                            filename=f"transcript-{interaction.channel.name}.html")

            channel = nextcord.utils.get(interaction.guild.channels, id=929275013851394058)                               
            message = await channel.send(file=transcript_file)
            await interaction.response.send_message(file=transcript_file)
            turl = message.attachments[0].url
            embed = nextcord.Embed(description=f"```TRANSCRIPT OF {interaction.channel.name}```\n\nThe Transcript file can be viewed by clicking on\n[This Link]({turl}) or from the button present belo, which will automatically download the transcript.html\nfile on your device and save you a few clicks or you can also download from the file above!")
            await channel.send(embed=embed,view=TDownload(turl))
        self.value=True

    @nextcord.ui.button(label = "Delete", style=nextcord.ButtonStyle.red, custom_id='del')
    async def dlose(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.guild_permissions.administrator is not True:
            await interaction.response.send_message('You are missing perms to delete the channel!',ephemeral=True)
        else:
            await interaction.response.send_message('Deleting the channel in 10 seconds!')
            await asyncio.sleep(10)
            await interaction.channel.delete()
            self.value=True

    @nextcord.ui.button(label = "Rename", style=nextcord.ButtonStyle.red, custom_id='rename')
    async def rlose(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        def check(msg):
            return msg.channel == interaction.channel and msg.author == interaction.user
        if interaction.user.guild_permissions.administrator is not True:
            await interaction.response.send_message('You are missing perms to rename the channel!',ephemeral=True)
        else:
            try:
                await interaction.response.send_message('What should be the new name of the channel?')
                msg = await client.wait_for('message',check=check,timeout=60)
                await interaction.channel.edit(name=msg.content)
                await interaction.response.send_message('Channel Successfully Renamed!')
            except asyncio.TimeoutError:
                await interaction.response.send_message('Timeout for responding!')
        self.value=True

class Tickett(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

  

    @nextcord.ui.button(emoji="<:Application:917722555891187742>",label = "Application", style=nextcord.ButtonStyle.gray, custom_id='modapp')
    async def gwt(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        
        drole = interaction.guild.get_role(918103961439965184)
        categ = nextcord.utils.get(interaction.guild.categories, id=918104018658684929)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
#remove
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await ticket_channel.set_permissions(drole, read_messages=True, send_messages=True)
        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Use >modapp for moderator application\n Use >ssapp for ticket support application\n Use >fxapp for fx judge application\n\nSupport will be with you soon!\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)
        
        self.value=True

    @nextcord.ui.button(emoji="<:DesignerApplication:917722714465267732>",label = "Designer-Application", style=nextcord.ButtonStyle.gray, custom_id='dznrapp')
    async def inv(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        srole = interaction.guild.get_role(918103951130365983)
        
        categ = nextcord.utils.get(interaction.guild.categories, id=918104018658684929)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True)
        await ticket_channel.set_permissions(srole, read_messages=True, send_messages=True)
        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n>app for designer application!\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)
        
        self.value=True
class TTP1(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

        
    @nextcord.ui.button(emoji="<:PaidTicket:917722571879903282>",label = "Paid Ticket", style=nextcord.ButtonStyle.gray, custom_id='paidapp')
    async def paidt(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ban_role=interaction.guild.get_role(932158497037103104)
        if ban_role in interaction.user.roles:
            await interaction.response.send_message(f'You have been blacklisted from creating this Ticket.', ephemeral=True)
            return
       	else:
            pass
        srole = interaction.guild.get_role(918103952090857482)
        orole = interaction.guild.get_role(918103966108233808)
        categ = nextcord.utils.get(interaction.guild.categories, id=932506029323866243)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
#remove
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await ticket_channel.set_permissions(srole, read_messages=True, send_messages=True)
        await ticket_channel.set_permissions(orole, read_messages=True, send_messages=True)
        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n Thanks for choosing Graphics Studio!\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)

    @nextcord.ui.button(emoji="<:InvitesTicket:917722610127753226>",label = "Invites Ticket", style=nextcord.ButtonStyle.gray, custom_id='invapp')
    async def invt(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ban_role=interaction.guild.get_role(932158497037103104)
        if ban_role in interaction.user.roles:
            await interaction.response.send_message(f'You have been blacklisted from creating this Ticket.', ephemeral=True)
            return
       	else:
            pass
        srole = interaction.guild.get_role(918103952090857482)
        orole = interaction.guild.get_role(918103966108233808)
        categ = nextcord.utils.get(interaction.guild.categories, id=918104010135834674)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
#remove
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await ticket_channel.set_permissions(srole, read_messages=True, send_messages=True)
        await ticket_channel.set_permissions(orole, read_messages=True, send_messages=True)
        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n Thanks for choosing Graphics Studio!\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)

    @nextcord.ui.button(emoji="<:BoosterTicket:917722777685999626>",label = "Booster Ticket", style=nextcord.ButtonStyle.gray, custom_id='boostapp')
    async def boostapp(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        ban_role=interaction.guild.get_role(932158497037103104)
        if ban_role in interaction.user.roles:
            await interaction.response.send_message(f'You have been blacklisted from creating this Ticket.', ephemeral=True)
            return
       	else:
            pass
        srole = interaction.guild.get_role(918103952090857482)
        orole = interaction.guild.get_role(918103966108233808)
        categ = nextcord.utils.get(interaction.guild.categories, id=932550337330544640)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
#remove
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await ticket_channel.set_permissions(srole, read_messages=True, send_messages=True)
        await ticket_channel.set_permissions(orole, read_messages=True, send_messages=True)
        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n Thanks for choosing Graphics Studio!\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)



    @nextcord.ui.button(emoji="<:GiveawayTicket:921411612102000690>",label = "Giveaway Ticket", style=nextcord.ButtonStyle.gray, custom_id='giveaway_ticket_app')
    async def giveaway_ticket(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        srole = interaction.guild.get_role(918103952090857482)
        orole = interaction.guild.get_role(918103966108233808)
        categ = nextcord.utils.get(interaction.guild.categories, id=918104010135834674)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
#remove
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await ticket_channel.set_permissions(srole, read_messages=True, send_messages=True)
        await ticket_channel.set_permissions(orole, read_messages=True, send_messages=True)
        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n Thanks For Choosing Graphics Studio\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)

class TTP3(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.value = None

  

    @nextcord.ui.button(emoji="<:AffiliateApplication:917722841414246400>",label = "Affiliation Ticket", style=nextcord.ButtonStyle.gray, custom_id='helpapp')
    async def ht(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):

        srole = interaction.guild.get_role(918103959879700480)
        categ = nextcord.utils.get(interaction.guild.categories, id=918104020579676170)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
#remove
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await ticket_channel.set_permissions(srole, view_channel=True, send_messages=True)

        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)
        
        self.value=True

    @nextcord.ui.button(emoji="<:HelpTicket:917722633506795550>",label = "General Help Ticket", style=nextcord.ButtonStyle.gray, custom_id='affapp')
    async def aft(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        srole = interaction.guild.get_role(918103959879700480)
        categ = nextcord.utils.get(interaction.guild.categories, id=918104020579676170)
        await interaction.response.send_message("Creating a ticket for you, this may take a while!", ephemeral=True)
        ticket_channel = await categ.create_text_channel(name=f"{button.label} {interaction.user.name}")
#remove
        await ticket_channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await ticket_channel.set_permissions(srole, view_channel=True, send_messages=True)

        view=Close()
        await ticket_channel.send(f"{interaction.user.mention}")
        embed = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n Please describe your problem in the chat!\n The **Close button** can only be used by staffs with manage messages perms!", color=0x5AFFBB )
        await ticket_channel.send(embed=embed, view=view)
        
        self.value=True

@client.command()
@commands.has_permissions(administrator=True)
async def ticketp1(ctx, channel: nextcord.TextChannel=None):
    view=TTP1()
    embed = nextcord.Embed()

    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author
    try:
        await ctx.send("Which ticket view do you want?\nReact with the buttons below!")
        await ctx.send("What should be the embed colour in hex code?Write `None` to skip, the color would be red from default!")
        msg = await client.wait_for('message', check=check,  timeout=60)

        if msg.content.lower() == 'none':
            embed.color = nextcord.Color.red()
        else:
            try:
                embed.colour = await commands.ColourConverter().convert(ctx, msg.content)
            except:
                return await ctx.send("Invalid Hex Code Provided! Please re-do the command!")
        await ctx.send("Please enter title!")
        msg = await client.wait_for('message',check = check,timeout= 60)
        embed.title = msg.content
        await ctx.send("Please enter description!")
        msg = await client.wait_for('message',check = check, timeout = 60)
        embed.description = msg.content
        await ctx.send("Please enter the url or write `None` to skip!")
        msg = await client.wait_for( 'message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_image(url=msg.content)
        await ctx.send("Alright! Now enter the thumbnail's url or write `None` to skip!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_thumbnail(url=msg.content)
        await ctx.send("Do you want the embed to have a footer? Write `None` to skip or `Yes` if you want it to have a footer!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("Embed Sent! Process completed")
            await channel.send(embed=embed, view=view)
            await view.wait()
        else:
            await ctx.send("Please enter the footer's icon url or write `None` to skip!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                pass
            else:
                embed.set_footer(icon_url=msg.content)
            await ctx.send("Please enter the footer's Content!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                await ctx.send("Foooter content cant be `None`! Please use the `>ticket` command again!")
                return

            else:
                embed.set_footer(text=msg.content)
                await ctx.send("Process Completed! Embed has been sent!")
                await channel.send(embed=embed, view=view)
                await view.wait()

        

    except asyncio.TimeoutError:
        await ctx.send("Timeout for responding!")
        return

@client.command()
@commands.has_permissions(administrator=True)
async def ticketp2(ctx, channel: nextcord.TextChannel):
    view=Tickett()
    embed = nextcord.Embed()

    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author
    try:
        await ctx.send("Which ticket view do you want?\nReact with the buttons below!")
        await ctx.send("What should be the embed colour in hex code?Write `None` to skip, the color would be red from default!")
        msg = await client.wait_for('message', check=check,  timeout=60)

        if msg.content.lower() == 'none':
            embed.color = nextcord.Color.red()
        else:
            try:
                embed.colour = await commands.ColourConverter().convert(ctx, msg.content)
            except:
                return await ctx.send("Invalid Hex Code Provided! Please re-do the command!")
        await ctx.send("Please enter title!")
        msg = await client.wait_for('message',check = check,timeout= 60)
        embed.title = msg.content
        await ctx.send("Please enter description!")
        msg = await client.wait_for('message',check = check, timeout = 60)
        embed.description = msg.content
        await ctx.send("Please enter the url or write `None` to skip!")
        msg = await client.wait_for( 'message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_image(url=msg.content)
        await ctx.send("Alright! Now enter the thumbnail's url or write `None` to skip!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_thumbnail(url=msg.content)
        await ctx.send("Do you want the embed to have a footer? Write `None` to skip or `Yes` if you want it to have a footer!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("Embed Sent! Process completed")
            await channel.send(embed=embed, view=view)
            await view.wait()
        else:
            await ctx.send("Please enter the footer's icon url or write `None` to skip!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                pass
            else:
                embed.set_footer(icon_url=msg.content)
            await ctx.send("Please enter the footer's Content!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                await ctx.send("Foooter content cant be `None`! Please use the `-ticket` command again!")
                return

            else:
                embed.set_footer(text=msg.content)
                await ctx.send("Process Completed! Embed has been sent!")
                await channel.send(embed=embed, view=view)
                await view.wait()

        

    except asyncio.TimeoutError:
        await ctx.send("Timeout for responding!")
        return

@client.command()
@commands.has_permissions(administrator=True)
async def ticketp3(ctx, channel: nextcord.TextChannel):
    view=TTP3()
    embed = nextcord.Embed()

    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author
    try:
        await ctx.send("Which ticket view do you want?\nReact with the buttons below!")
        await ctx.send("What should be the embed colour in hex code?Write `None` to skip, the color would be red from default!")
        msg = await client.wait_for('message', check=check,  timeout=60)

        if msg.content.lower() == 'none':
            embed.color = nextcord.Color.red()
        else:
            try:
                embed.colour = await commands.ColourConverter().convert(ctx, msg.content)
            except:
                return await ctx.send("Invalid Hex Code Provided! Please re-do the command!")
        await ctx.send("Please enter title!")
        msg = await client.wait_for('message',check = check,timeout= 60)
        embed.title = msg.content
        await ctx.send("Please enter description!")
        msg = await client.wait_for('message',check = check, timeout = 60)
        embed.description = msg.content
        await ctx.send("Please enter the url or write `None` to skip!")
        msg = await client.wait_for( 'message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_image(url=msg.content)
        await ctx.send("Alright! Now enter the thumbnail's url or write `None` to skip!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_thumbnail(url=msg.content)
        await ctx.send("Do you want the embed to have a footer? Write `None` to skip or `Yes` if you want it to have a footer!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("Embed Sent! Process completed")
            await channel.send(embed=embed, view=view)
            await view.wait()
        else:
            await ctx.send("Please enter the footer's icon url or write `None` to skip!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                pass
            else:
                embed.set_footer(icon_url=msg.content)
            await ctx.send("Please enter the footer's Content!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                await ctx.send("Foooter content cant be `None`! Please use the `-ticket` command again!")
                return

            else:
                embed.set_footer(text=msg.content)
                await ctx.send("Process Completed! Embed has been sent!")
                await channel.send(embed=embed, view=view)
                await view.wait()

        

    except asyncio.TimeoutError:
        await ctx.send("Timeout for responding!")
        return
    
class Panel4(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label='1', style=nextcord.ButtonStyle.grey, custom_id='persistent_view:green')
    async def panelfourusd(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("""<a:starwhite:917723116078264330>𝚄𝚂𝙳 ($)

<a:Nitro:917723044292726824>AVI :- 1$
<a:Nitro:917723044292726824>Concept Logo :- 2$
<a:Nitro:917723044292726824>Logo Edit :- 10$ [5 Pieces]
<a:Nitro:917723044292726824>Discord Banner :- 1$
<a:Nitro:917723044292726824>Header :- 1$
<a:Nitro:917723044292726824>Intro & Outro :- 3$
<a:Nitro:917723044292726824>Jersey :- 3$
<a:Nitro:917723044292726824>Mascot Logo :- 2$
<a:Nitro:917723044292726824>Montage :- 4$
<a:Nitro:917723044292726824>Motion Graphics :- 5$
<a:Nitro:917723044292726824>Overlay :- 2$/3$ [Static/Animated]
<a:Nitro:917723044292726824>Poster :- 2$
<a:Nitro:917723044292726824>PFP :- 1$
<a:Nitro:917723044292726824>Roster :- 2$
<a:Nitro:917723044292726824>Server Icon :- 1$/2$ [Static/Animated]
<a:Nitro:917723044292726824>Server Setup :- 4$
<a:Nitro:917723044292726824>Stinger :- 3$
<a:Nitro:917723044292726824>Thumbnail :- 2$
<a:Nitro:917723044292726824>Vector :- 2$
<a:Nitro:917723044292726824>Wallpaper :- 1$
<a:Nitro:917723044292726824>YouTube Banner :- 2$
""", ephemeral=True)

    @nextcord.ui.button(label='2', style=nextcord.ButtonStyle.grey, custom_id='persistent_view:red')
    async def panel4inv(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("""<a:starwhite:917723116078264330>𝙸𝚗𝚟𝚒𝚝𝚎𝚜

<a:Nitro:917723044292726824>AVI :- 10 Invites
<a:Nitro:917723044292726824>Concept Logo :- 10 Invites
<a:Nitro:917723044292726824>Logo Edit :- 10 Invites [1 Piece]
<a:Nitro:917723044292726824>Discord Banner :- 10 Invites
<a:Nitro:917723044292726824>Header :- 10 Invites
<a:Nitro:917723044292726824>Intro & Outro :- 15 Invites
<a:Nitro:917723044292726824>Jersey :- 15 Invites
<a:Nitro:917723044292726824>Mascot Logo :- 10 Invites
<a:Nitro:917723044292726824>Montage :- 20 Invites
<a:Nitro:917723044292726824>Motion Graphics :- 25 Invites
<a:Nitro:917723044292726824>Overlay :- 10 Invites/15 Invites [Static/Animated]
<a:Nitro:917723044292726824>Poster :- 10 Invites
<a:Nitro:917723044292726824>PFP :- 10 Invites
<a:Nitro:917723044292726824>Roster :- 10 Invites
<a:Nitro:917723044292726824>Server Icon :- 10 Invites/15 Invites [Static/Animated]
<a:Nitro:917723044292726824>Server Setup :- 20 Invites
<a:Nitro:917723044292726824>Stinger :- 15 Invites
<a:Nitro:917723044292726824>Thumbnail :- 10 Invites
<a:Nitro:917723044292726824>Vector :- 10 Invites
<a:Nitro:917723044292726824>Wallpaper :- 10 Invites
<a:Nitro:917723044292726824>YouTube Banner :- 10 Invites""", ephemeral=True)

    

    @nextcord.ui.button(label='3', style=nextcord.ButtonStyle.grey, custom_id='persistent_view:gr')
    async def panel4boosterperks(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("""<a:starpink:917723124903079947> 𝙱𝚘𝚘𝚜𝚝𝚎𝚛 𝙿𝚎𝚛𝚔𝚜

𝚂𝚒𝚗𝚐𝚕𝚎 𝙱𝚘𝚘𝚜𝚝 <a:heart_white:917722989942947850>

<a:Nitro:917723044292726824> Order any 1 GFX every 10 days
<a:Nitro:917723044292726824> Customised Server Booster role
<a:Nitro:917723044292726824> Special message in Nitro Boosters

𝙼𝚞𝚕𝚝𝚒𝚙𝚕𝚎 𝙱𝚘𝚘𝚜𝚝𝚜 <a:Heart_pink:917722981030043659>

<a:Nitro:917723044292726824> Order any 2 FX every 10 days (No. of Fx increases as number of boosts increase)
<a:Nitro:917723044292726824> Customised Server Booster role
<a:Nitro:917723044292726824> Special message in Nitro Boosters
<a:Nitro:917723044292726824> Promotion in Booster Promotion with @here ping
<a:Nitro:917723044292726824> Customisable Graphics Studio Jersey {Minimum 3 boosts}
""", ephemeral=True)

    @nextcord.ui.button(label='4', style=nextcord.ButtonStyle.grey, custom_id='persistent_view:grey')
    async def panel4streamerpack(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("""<a:starblue:917723136747769857> 𝚂𝚝𝚛𝚎𝚊𝚖𝚎𝚛 𝙿𝚊𝚌𝚔

<a:Nitro:917723044292726824>PFP :- 1$
<a:Nitro:917723044292726824>Overlay :- 2$
<a:Nitro:917723044292726824>Stinger :- 3$
<a:Nitro:917723044292726824>Stream Starting Soon :- 2$
<a:Nitro:917723044292726824>Stream will be back soon :- 2$
<a:Nitro:917723044292726824>Stream has ended :- 1$
<a:Nitro:917723044292726824>Thumbnail :- 2$
<a:Nitro:917723044292726824>YouTube Banner :- 2$

𝚃𝚘𝚝𝚊𝚕 :- 𝟷5$ 
𝙽𝚘𝚠 𝚊𝚝 10$ /- <a:heart_white:917722989942947850>
""", ephemeral=True)

    @nextcord.ui.button(label='5', style=nextcord.ButtonStyle.grey, custom_id='persistent_view:')
    async def panel4clanpack(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("""<a:starblue:917723136747769857> 𝙲𝚕𝚊𝚗 𝙿𝚊𝚌𝚔

<a:Nitro:917723044292726824>Concept Logo :- 2$
<a:Nitro:917723044292726824>Concept Logo Edit :- 10$ [1 piece]
<a:Nitro:917723044292726824>Metallic AVI :- 5$ [5 Pieces]
<a:Nitro:917723044292726824>Jersey :- 3$
<a:Nitro:917723044292726824>Roster :- 2$
<a:Nitro:917723044292726824>Server Icon :- 1$
<a:Nitro:917723044292726824>Server Setup :- 4$

𝚃𝚘𝚝𝚊𝚕 :- 27$
𝙽𝚘𝚠 𝚊𝚝 25$/- <a:heart_white:917722989942947850>
""", ephemeral=True)

    @nextcord.ui.button(label='6', style=nextcord.ButtonStyle.grey, custom_id='persistent_view:g')
    async def panel4youtuberperk(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("""<a:starblue:917723136747769857> 𝚈𝚘𝚞𝚃𝚞𝚋𝚎𝚛 𝙿𝚊𝚌𝚔

<a:Nitro:917723044292726824>PFP :- 1$
<a:Nitro:917723044292726824>Intro & Outro :- 3$
<a:Nitro:917723044292726824>Montage Edit :- 4$
<a:Nitro:917723044292726824>Thumbnail :- 2$
<a:Nitro:917723044292726824>YouTube Banner :- 2$

𝚃𝚘𝚝𝚊𝚕 :- 12$
𝙽𝚘𝚠 𝚊𝚝  10$/- <a:heart_white:917722989942947850>
""", ephemeral=True)

class Panel5(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(label='Bot Ticket', emoji='<:BotTicket:932704236318363738>', custom_id='Bot Ticket')
    async def BotTicket(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        categ= nextcord.utils.get(interaction.guild.categories, id=932506029323866243)
        chann = await categ.create_text_channel(name=f'bot-ticket-{interaction.user.name}')
        staff=nextcord.utils.get(interaction.guild.roles, id=918103959879700480)
        oth=nextcord.utils.get(interaction.guild.roles, id=918103960710156298)
        await chann.set_permissions(interaction.user, view_channel=True, send_messages=True)
        await chann.set_permissions(oth, view_channel=True, send_messages=True)
        await chann.set_permissions(staff, view_channel=True, send_messages=True)
        await chann.send(f"{interaction.user.mention}")
        view=Close()
        emb = nextcord.Embed(title=f"Support Needed!", description=f"A ticket opened by **{interaction.user.name}**,\n Server Display name is **{interaction.user.display_name}**\n Support will be with you soon!\n The **Close button** can only be used by staffs with manage messages perms!", color=nextcord.Color(0x5AFFBB) )
        await chann.send(embed=emb, view=view)

@client.command()
@commands.has_permissions(administrator=True)
async def ticketp5(ctx, channel: nextcord.TextChannel):
    embed=nextcord.Embed()
    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author
    try:
        await ctx.send("What should be the embed colour in hex code?Write `None` to skip, the color would be red from default!")
        msg = await client.wait_for('message', check=check,  timeout=60)

        if msg.content.lower() == 'none':
            embed.color = nextcord.Color.red()
        else:
            try:
                embed.colour = await commands.ColourConverter().convert(ctx, msg.content)
            except:
                return await ctx.send("Invalid Hex Code Provided! Please re-do the command!")
        await ctx.send("Please enter title!")
        msg = await client.wait_for('message',check = check,timeout= 60)
        embed.title = msg.content
        await ctx.send("Please enter description!")
        msg = await client.wait_for('message',check = check, timeout = 60)
        embed.description = msg.content
        await ctx.send("Please enter the url or write `None` to skip!")
        msg = await client.wait_for( 'message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_image(url=msg.content)
        await ctx.send("Alright! Now enter the thumbnail's url or write `None` to skip!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_thumbnail(url=msg.content)
        await ctx.send("Do you want the embed to have a footer? Write `None` to skip or `Yes` if you want it to have a footer!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("Embed Sent! Process completed")
            view=Panel5()
            await channel.send(embed=embed, view=view)
        else:
            await ctx.send("Please enter the footer's icon url or write `None` to skip!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                pass
            else:
                embed.set_footer(icon_url=msg.content)
            await ctx.send("Please enter the footer's Content!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                await ctx.send("Foooter content cant be `None`! Please use the `-ticket` command again!")
                return

            else:
                embed.set_footer(text=msg.content)
                await ctx.send("Process Completed! Embed has been sent!")
                view=Panel5()
                await channel.send(embed=embed, view=view)

    except asyncio.TimeoutError:
        await ctx.send("Timeout for responding!")
        return

@client.command()
@commands.has_permissions(administrator=True)
async def adduser(ctx, user:nextcord.Member=None):
    print(f'Testing')
    try:
        await ctx.channel.set_permissions(user, view_channel=True, send_messages=True, send_files=True)
        print(f'worked')
    except:
        print('error')
@client.command()
@commands.has_permissions(administrator=True)
async def ticketp4(ctx, channel: nextcord.TextChannel):
    view=Panel4()
    embed = nextcord.Embed()

    def check(msg):
        return msg.channel == ctx.channel and msg.author == ctx.author
    try:
        await ctx.send("Which ticket view do you want?\nReact with the buttons below!")
        await ctx.send("What should be the embed colour in hex code?Write `None` to skip, the color would be red from default!")
        msg = await client.wait_for('message', check=check,  timeout=60)

        if msg.content.lower() == 'none':
            embed.color = nextcord.Color.red()
        else:
            try:
                embed.colour = await commands.ColourConverter().convert(ctx, msg.content)
            except:
                return await ctx.send("Invalid Hex Code Provided! Please re-do the command!")
        await ctx.send("Please enter title!")
        msg = await client.wait_for('message',check = check,timeout= 60)
        embed.title = msg.content
        await ctx.send("Please enter description!")
        msg = await client.wait_for('message',check = check, timeout = 60)
        embed.description = msg.content
        await ctx.send("Please enter the url or write `None` to skip!")
        msg = await client.wait_for( 'message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_image(url=msg.content)
        await ctx.send("Alright! Now enter the thumbnail's url or write `None` to skip!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            pass
        else:

            embed.set_thumbnail(url=msg.content)
        await ctx.send("Do you want the embed to have a footer? Write `None` to skip or `Yes` if you want it to have a footer!")
        msg = await client.wait_for('message', check=check, timeout=60)
        if msg.content.lower() == 'none':
            await ctx.send("Embed Sent! Process completed")
            await channel.send(embed=embed, view=view)
            await view.wait()
        else:
            await ctx.send("Please enter the footer's icon url or write `None` to skip!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                pass
            else:
                embed.set_footer(icon_url=msg.content)
            await ctx.send("Please enter the footer's Content!")
            msg = await client.wait_for('message', check=check, timeout=60)
            if msg.content.lower() == 'none':
                await ctx.send("Foooter content cant be `None`! Please use the `-ticket` command again!")
                return

            else:
                embed.set_footer(text=msg.content)
                await ctx.send("Process Completed! Embed has been sent!")
                await channel.send(embed=embed, view=view)
                await view.wait()

        

    except asyncio.TimeoutError:
        await ctx.send("Timeout for responding!")
        return
    
client.run("OTA1ODM5NTY4NDAwNTc2NTM0.YYP61g.FkV5fTAe3hcNKIvRcU9dllXSAHg")
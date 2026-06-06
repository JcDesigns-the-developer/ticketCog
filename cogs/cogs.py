import discord
from discord.ext import commands
class TicketSystem(commands.Cog):
    “”“
    A cog for managing a ticket system in a Discord bot using Pycord.
    “”“
def __init__(self, bot):
    self.bot = bot
    self.blacklist = set()  # Set to hold blacklisted user IDs

@commands.command()
async def setup(self, ctx):
    """
    Sets up the ticket system by creating necessary channels and roles.
    """
    # Create a category for tickets
    category = await ctx.guild.create_category("Tickets")
    await ctx.send(f"Ticket category '{category.name}' created.")

@commands.command()
async def close(self, ctx):
    """
    Closes the ticket channel where the command is invoked.
    """
    if ctx.channel.category and ctx.channel.category.name == "Tickets":
        await ctx.channel.send("This ticket will be closed.")
        await ctx.channel.delete()
    else:
        await ctx.send("This command can only be used in a ticket channel.")

@commands.command()
async def closerequest(self, ctx):
    """
    Requests to close the ticket. This can be used to notify staff.
    """
    await ctx.send("A request to close this ticket has been sent.")

@commands.command()
async def add(self, ctx, member: discord.Member):
    """
    Adds a member to the ticket channel.
    """
    await ctx.channel.set_permissions(member, read_messages=True, send_messages=True)
    await ctx.send(f"{member.mention} has been added to the ticket.")

@commands.command()
async def remove(self, ctx, member: discord.Member):
    """
    Removes a member from the ticket channel.
    """
    await ctx.channel.set_permissions(member, read_messages=False, send_messages=False)
    await ctx.send(f"{member.mention} has been removed from the ticket.")

@commands.command()
async def ticket_blacklist_add(self, ctx, member: discord.Member):
    """
    Adds a member to the ticket blacklist.
    """
    self.blacklist.add(member.id)
    await ctx.send(f"{member.mention} has been added to the ticket blacklist.")

@commands.command()
async def ticket_blacklist_remove(self, ctx, member: discord.Member):
    """
    Removes a member from the ticket blacklist.
    """
    self.blacklist.discard(member.id)
    await ctx.send(f"{member.mention} has been removed from the ticket blacklist.")

async def setup(bot):
    await bot.add_cog(TicketSystem(bot))

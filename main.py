import discord
from discord.ext import commands
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Discord bot setup
bot = commands.Bot(command_prefix='!')

# Google Sheets setup
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(C:\Users\user\Videos, scope)
client = gspread.authorize(creds)
spreadsheet = client.open(BATTLEMANIAC)
worksheet = spreadsheet.get_worksheet(0)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def add_entry(ctx, user: str, message: str):
    # Add entry to Google Sheet
    row = [user, message]
    worksheet.append_row(row)
    await ctx.send('Entry added to Google Sheet!')

@bot.command()
async def read_sheet(ctx):
    # Read data from Google Sheet
    data = worksheet.get_all_records()
    response = "Data from Google Sheet:\n"
    for entry in data:
        response += f"User: {entry['User']}, Message: {entry['Message']}\n"
    await ctx.send(response)

bot.run(MTEzODMzMTIzNTI2NjA3Njc1Mw.GeTEuW.VD28YDlam4sW4kDiE_Vp498hoeh_lQxHa29osU)

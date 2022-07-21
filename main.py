import requests, random 
from discord_webhook import DiscordWebhook, DiscordEmbed # pip install discord_webhook
print('''\x1b[34m
  ║██║                              ██╗ ║██████╗
  ║██║                              ██║ ║██╔══██╗
  ║██║         ║██   ██║  ║██████   ██║ ║██║  ██║ 
  ║██║         ║██   ██║  ║██║╔══╗  ██║ ║██║  ██║
    ║█████████  ╚ ███ ╔╝  ║██████ ║ ██║ ║██████╔╝
    ╚════════╝  ╚═════╝   ╚══════╝  ╚═╝  ╚═════╝
''')
print("\x1b[32mSTAR THE REPO ON GITHUB ! \x1b[39m")
while True:
        ID = random.randint(10800000, 10960000) # Start and stop IDs edit this if you want!
        webhook = DiscordWebhook(url="Put Your Wenhook Here") # initates connection with discord_webhook module
        r = requests.get(f'https://groups.roblox.com/v1/groups/{ID}') #sends requests using id
        json = r.json() # json
        if 'owner' in r.text: #checks if the group is valid to prevent key errors
                if json['owner'] == None and json['publicEntryAllowed'] == True and 'isLocked' not in r.text: # check if the group isnt locked and is open with no owner
                        members = json['memberCount'] #members
                        desc = json['description'] #obvious what this one is
                        print(f"\x1b[42mhttps://www.roblox.com/groups/{ID}")
                        print(r.text)
                        embed = DiscordEmbed(title='New unclaimed Group', color=242424) # embed title
                        embed.add_embed_field(name='ID', value=f'{ID}') #Id to embed
                        embed.add_embed_field(name='Description', value=f'"{desc}"') #description to embed
                        embed.add_embed_field(name='Members', value=f'{members}') #adds members to embed
                        embed.add_embed_field(name='Link', value=f'https://www.roblox.com/groups/{ID}') # im getting bored commenting
                        embed.set_author(name='', icon_url='https://cdn.discordapp.com/attachments/984864841380532266/991331975161978900/Lucid.gif') #stuff
                        embed.set_footer(text='Lucid', icon_url='https://cdn.discordapp.com/attachments/984864841380532266/991331975161978900/Lucid.gif') # stuff
                        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/984864841380532266/991331975161978900/Lucid.gif')
                        webhook.add_embed(embed) #adds the embed to the response
                        response = webhook.execute() # sends to webhook
                else:
                        print(f"\x1b[31mNothing found... https://discord.gg/zupKSnyRNg {ID}")                     
        else:
                print(f"\x1b[31mNothing found... https://discord.gg/zupKSnyRNg {ID}")      

import nextcord
from nextcord.ext import commands
from nextcord import Interaction
import random
import string
token = # token do bot

# Configuração do bot com intents de conteúdo de mensagem habilitados
intents = nextcord.Intents.default()
intents.message_content = True  # Habilita o acesso ao conteúdo das mensagens

bot = commands.Bot(command_prefix="!", intents=intents)

# Função para gerar strings aleatórias
def generate_string(length=86):
    chars = string.ascii_letters + string.digits + '+/='
    return ''.join(random.choice(chars) for _ in range(length))

# Comando de barra para gerar strings
@bot.slash_command(name="generate_strings", description="Gera strings aleatórias.")
async def generate_strings(interaction: Interaction, quantity: int):
    if quantity < 1 or quantity > 100:
        await interaction.response.send_message("Por favor, escolha uma quantidade entre 1 e 100.")
        return

    generated_strings = [generate_string() for _ in range(quantity)]
    await interaction.response.send_message("\n".join(generated_strings))

# Comando de barra para customizar e gerar strings
@bot.slash_command(name="custom_generate", description="Gera strings com customização.")
async def custom_generate(interaction: Interaction, quantity: int, length: int = 86, charset: str = "default"):
    if quantity < 1 or quantity > 23:
        await interaction.response.send_message("Por favor, escolha uma quantidade entre 1 e 23.")
        return

    if charset == "default":
        chars = string.ascii_letters + string.digits + '+/='
    elif charset == "letters":
        chars = string.ascii_letters
    elif charset == "digits":
        chars = string.digits
    else:
        chars = charset

    generated_strings = [''.join(random.choice(chars) for _ in range(length)) for _ in range(quantity)]
    await interaction.response.send_message("\n".join(generated_strings))

# Função para rodar o bot
bot.run(token)

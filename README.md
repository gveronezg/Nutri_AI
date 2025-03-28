# Nutri_AI 🤖

Um assistente virtual nutricional inteligente que oferece orientações personalizadas sobre alimentação e nutrição através do Telegram.

## 📋 Descrição

O Nutri_AI é um bot do Telegram que utiliza inteligência artificial avançada para fornecer orientações nutricionais personalizadas. O bot é capaz de:

- Responder perguntas sobre nutrição e alimentação
- Analisar fotos de pratos e refeições
- Fornecer recomendações personalizadas
- Manter histórico de conversas para melhor atendimento
- Oferecer dicas baseadas em diferentes dietas (mediterrânea, cetogênica, ayurvédica)

## 🚀 Funcionalidades

- **Chat Inteligente**: Interação natural com o usuário
- **Análise de Imagens**: Capacidade de analisar fotos de alimentos
- **Histórico Persistente**: Mantém o contexto das conversas
- **Respostas Personalizadas**: Adapta as respostas ao perfil do usuário
- **Orientação Nutricional**: Fornece informações detalhadas sobre nutrientes

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- LangChain
- OpenAI GPT-4
- Pyrogram (Telegram Bot API)
- SQLite (para armazenamento de histórico)
- Pillow (para processamento de imagens)

## ⚙️ Configuração

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/Nutri_AI.git
cd Nutri_AI
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
TELEGRAM_API_ID=seu_api_id
TELEGRAM_API_HASH=seu_api_hash
TELEGRAM_TOKEN=seu_token
OPENAI_API_KEY=sua_chave_api
```

4. Execute o bot:
```bash
python app.py
```

## 📱 Como Usar

1. Inicie uma conversa com o bot no Telegram usando /start
2. Envie mensagens com perguntas sobre nutrição
3. Envie fotos de pratos para análise nutricional
4. Receba orientações personalizadas e recomendações

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, siga estes passos:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- Gabriel V.G. - [@gveronezg](https://github.com/gveronezg)

## 🙏 Agradecimentos

- Asimov Academy pelos ensinamentos
- OpenAI por fornecer a API GPT-4
- Comunidade do Telegram por suas APIs
- Todos os contribuidores do projeto
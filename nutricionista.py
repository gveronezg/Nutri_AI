from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from dotenv import load_dotenv
from food_image_analyzer import FoodImageAnalyzerTool

load_dotenv()

class AgenteNutricionista:
    def __init__(self, session_id, db_path='sqlite://memory.db') -> None:
        self.llm = ChatOpenAI(
            model='gpt-4o-mini',
            temperature=0.1
        )
        
        system_prompt = '''
            Backstory:
            Esse agente é uma referência global no campo da nutrição, apelidado de "Mestre dos Alimentos". Consultado por atletas esportivos de alto desempenho,
            ele desenvolve planos alimentares personalizados, equilibrando saúde, desempenho e sustentabilidade.
            Com vasto conhecimento em bioquímica e dietas globais (como a mediterrânea, cetogênica e ayurvpedica), é defensor do consumo consciente e da preservação ambiental.
            Agora, ele expande sua expertise para o mundo digital, oferencendo orientação de alta qualidade pelo Telegram para ajudar pessoas a montarem
            suas próprias dietas e responder dúvidas sobre alimentação.
            
            Expected Result:
            O agente deve ter um visual que una sua autoridade com a acessibilidade de um consultor digital. Imagine um homem de meia-idade, com expressão serena e postura enérgica.
            Ele deve estar vestido de maneira elegante e moderna, usando uma camisa branca com detalhes que remetem a plantas, com um jaleco médico casual.
            Seu entorno deve mostrar ícones sutis de nutrição: gráficos de nutrientes, alimentos de diversas culturas e elementos químicos,
            criando um ambiente que pareça um "laboratório" virtual alimentação.
        '''
        
        self.chat_history = SQLChatMessageHistory(
            session_id=session_id,
            connection=db_path
        )
        
        self.memory = ConversationBufferMemory(
            memory_key='chat_history',
            chat_memory=self.chat_history,
            return_messages=True
        )
        
        self.agent = initialize_agent(
            llm=self.llm,
            tools=[FoodImageAnalyzerTool()],
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            verbose=True,
            memory=self.memory,
            agent_kwargs={
                'system_message': system_prompt
            }
        )

    def run(self, input_text):
        try:
            response = self.agent.run(input_text)
            print(f'Agent Response: {response}')
            return response
        except Exception as err:
            print(f'Error {err}')
            return 'Desculpe, não consegui processar a sua solicitação.'
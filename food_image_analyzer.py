import base64
from io import BytesIO
from langchain.tools import BaseTool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from PIL import Image

class FoodImageAnalyzerTool(BaseTool):
    name: str = 'food_image_analyzer'
    description: str = '''
        Utilize esta ferramenta para analisar imagens de identificar alimentos que o usuário apresentar. Descreva os alimentos presentes e crie uma tabela nutricional com base neles.
        O agente deve usar esta ferramenta sempre que um caminho de imagem for fornecido, mas somente quando o input for um caminho de imagem.
    '''
    
    def __init__(self):
        super().__init__()
        
    def _run(self, image_path: str):
        image = Image.open(image_path)
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        instructions = """
            Você deve analisar a imagem enviada e verificar se ela contém alimentos.
            Caso contenha alimentos, descreva os itens visíveis e crie uma descrição nutricional detalhada e estimada
            incluindo calorias, carboidratos, proteínas e gorduras. Forneça uma descrição nutricional completa das possiveis refeições.
        """
        llm = ChatOpenAI(model='gpt-4o-mini')
        message = [HumanMessage(
            content=[
                {'type': 'text', 'text': instructions},
                {'type': 'image_url', 'image_url': {'url': f"data:image/jpeg;base64,{img_b64}"}}
            ]
        )]
        
        response = llm.invoke(message)
        return response
        
    async def _arun(self, image_path: str) -> str:
        raise NotImplementedError("Execução assíncrona não suportada.")
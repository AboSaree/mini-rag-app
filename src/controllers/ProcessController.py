from fastapi import UploadFile
from .BaseController import BaseController
from .ProjectController import ProjectController
from models.Enums import ResponseEnums,ExtensionEnums
import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
class ProcessController(BaseController):
    def __init__(self,project_id:str):
        super().__init__()
        self.project_id = project_id
        self.project_path = ProjectController().get_project_dir(project_id=project_id)


    def getFileExtension(self, file_id:str):
        file_extension = os.path.splitext(file_id)[-1]
        return file_extension
    
    def getFileLoader(self, file_id : str):
        file_extension = self.getFileExtension(file_id=file_id)
        file_path = os.path.join(self.project_path, file_id)
        if file_extension == ".pdf":
            loader = PyMuPDFLoader(file_path)
        elif file_extension == ".txt":
            loader = TextLoader(file_path)
        else:
            return None
        return loader
    
    def getFileContent(self, file_id : str):
        loader = self.getFileLoader(file_id=file_id)
        return loader.load()
    
    def processFileContent(self, file_id : str,file_content : list,
                           chunk_size : int = 100, chunk_overlap : int = 20):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                        chunk_overlap=chunk_overlap,
                                                        length_function=len)
        file_content = self.getFileContent(file_id=file_id)
        
        file_content_text = [
            rec.page_content
            for rec in file_content
        ]
        file_content_metadata = [
            rec.metadata
            for rec in file_content
        ]

        chunks = text_splitter.create_documents(file_content_text,metadatas=file_content_metadata)
        return chunks
        
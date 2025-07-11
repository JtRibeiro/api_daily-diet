
# 🥗 API Daily Diet

Uma API RESTful simples e eficiente para gerenciamento de dietas diárias, permitindo operações CRUD (Create, Read, Update, Delete) para registrar e consultar informações sobre diferentes tipos de dietas. Ideal para aplicações de saúde, bem-estar ou gerenciamento pessoal que necessitem de um backend robusto e fácil de integrar.

---

## ✨ Funcionalidades

- **Criação de Dietas** (`POST /diet`): Adicione novas dietas com nome, descrição e status de atividade.  
- **Listagem de Dietas** (`GET /diets`): Recupere todas as dietas cadastradas no sistema.  
- **Consulta de Dieta por ID** (`GET /diet/<id_diet>`): Obtenha os detalhes de uma dieta específica.  
- **Atualização de Dieta** (`PUT /diet/<id_diet>`): Modifique informações de uma dieta existente (atualização parcial).  
- **Exclusão de Dieta** (`DELETE /diet/<id_diet>`): Remova uma dieta do sistema.  

---

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.  
- **Flask**: Microframework web para construção da API.  
- **Flask-SQLAlchemy**: ORM para facilitar a interação com o banco de dados.  
- **SQLite**: Banco de dados leve e embutido, ideal para testes e desenvolvimento.

---

## 📦 Estrutura do Projeto

```
api_daily-diet/
├── app.py                  # Ponto de entrada da aplicação Flask e rotas da API
├── database.py             # Configuração do SQLAlchemy e instância do banco de dados
├── model/
│   └── diet.py             # Definição do modelo de dados para a Dieta
├── .env                    # Variáveis de ambiente (opcional)
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

## ⚙️ Configuração e Execução

### ✅ Pré-requisitos

- Python 3.9 ou superior

### 1. Clonar o Repositório

```bash
git clone https://github.com/JtRibeiro/api_daily-diet.git
cd api_daily-diet
```

### 2. Criar e Ativar o Ambiente Virtual

```bash
python -m venv venv
# No Windows
.env\Scriptsctivate
# No macOS/Linux
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

Se ainda não existir o arquivo `requirements.txt`, crie-o com:

```
Flask
Flask-SQLAlchemy
```

### 4. Configurar Variáveis de Ambiente (opcional)

Crie um arquivo `.env` na raiz do projeto:

```env
SECRET_KEY="sua_chave_secreta_aqui"
```

> Para usar o `.env`, instale a lib `python-dotenv`:
> ```bash
> pip install python-dotenv
> ```
> E adicione no início do `app.py`:
> ```python
> from dotenv import load_dotenv
> load_dotenv()
> ```

### 5. Inicializar o Banco de Dados

O banco `database.db` será criado automaticamente na primeira execução, se não existir.

### 6. Executar a Aplicação

```bash
python app.py
```

A API estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📚 Endpoints da API

### 🔹 POST `/diet` – Criar uma nova dieta

**Corpo da Requisição (JSON):**
```json
{
  "name": "Dieta Mediterrânea",
  "description": "Foco em vegetais, azeite e peixes.",
  "is_active": true
}
```

**Respostas:**

- ✅ `201 Created`:
```json
{
  "id": 1,
  "name": "Dieta Mediterrânea",
  "description": "Foco em vegetais, azeite e peixes.",
  "is_active": true
}
```

- ❌ `400 Bad Request`:
```json
{
  "message": "Campo name é obrigatório!"
}
```

---

### 🔹 GET `/diets` – Listar todas as dietas

**Resposta:**

- ✅ `200 OK`:
```json
{
  "diets": [
    {
      "id": 1,
      "name": "Dieta Mediterrânea",
      "description": "Foco em vegetais, azeite e peixes.",
      "is_active": true
    },
    {
      "id": 2,
      "name": "Dieta Low Carb",
      "description": "Redução de carboidratos.",
      "is_active": true
    }
  ],
  "total_diet": 2
}
```

- ❌ `404 Not Found`:
```json
{
  "message": "Nenhuma dieta cadastrada no sistema!"
}
```

---

### 🔹 GET `/diet/<id_diet>` – Consultar dieta por ID

**Resposta:**

- ✅ `200 OK`:
```json
{
  "id": 1,
  "name": "Dieta Mediterrânea",
  "description": "Foco em vegetais, azeite e peixes.",
  "is_active": true
}
```

- ❌ `404 Not Found`:
```json
{
  "message": "Dieta não cadastrada no sistema!"
}
```

---

### 🔹 PUT `/diet/<id_diet>` – Atualizar uma dieta

**Corpo da Requisição (JSON):**
```json
{
  "name": "Dieta Mediterrânea Atualizada",
  "is_active": false
}
```

**Resposta:**

- ✅ `200 OK`:
```json
{
  "id": 1,
  "name": "Dieta Mediterrânea Atualizada",
  "description": "Foco em vegetais, azeite e peixes.",
  "is_active": false
}
```

- ❌ `404 Not Found`:
```json
{
  "message": "Dieta não cadastrada no sistema!"
}
```

---

### 🔹 DELETE `/diet/<id_diet>` – Deletar uma dieta

**Resposta:**

- ✅ `200 OK`:
```json
{
  "message": "A Dieta 1 foi deletado com sucesso!"
}
```

- ❌ `404 Not Found`:
```json
{
  "message": "Dieta para deleção não cadastrada no sistema!"
}
```

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Se você tiver sugestões, melhorias ou encontrar bugs:

1. Faça um **fork** do projeto  
2. Crie uma nova branch:  
   `git checkout -b feature/sua-feature`  
3. Commit suas alterações:  
   `git commit -m 'feat: Adiciona nova funcionalidade X'`  
4. Push para o repositório:  
   `git push origin feature/sua-feature`  
5. Abra um **Pull Request** 🚀

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT**.  
Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

## 📧 Contato

**Jair Torezone (JtRibeiro)**  
📩 Email: [jairtorezone@gmail.com](mailto:jairtorezone@gmail.com)  
🔗 Projeto no GitHub: [https://github.com/JtRibeiro/api_daily-diet](https://github.com/JtRibeiro/api_daily-diet)

# Changelog

Todas as alterações relevantes deste projeto serão documentadas neste arquivo.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [Unreleased] — Branch `refactor/otimize-request-supabase`

> Comparado com: `origin/main` (GitHub — https://github.com/IGUHH/Bora_Contar_Pessoas)

---

### Adicionado

- **Dashboard Web (Tempo Real):**
  - **`src/app.py`** — Servidor web local criado com Flask para hospedar a interface.
  - **`src/templates/index.html`** — Painel em HTML/JS com Chart.js que se conecta via API REST diretamente ao Supabase e atualiza o gráfico de detecções a cada 2 segundos.
- **`requirements.txt`** — Arquivo de dependências criado com os pacotes necessários (`ultralytics`, `opencv-python`, `supabase`, `python-dotenv`, `flask`).
- **`CHANGELOG.md`** — Este arquivo de changelog do projeto.

---

### Alterado

- **`requirements.txt`** — Fixado com as versões exatas de todas as dependências e subdependências (gerado com `pip freeze`).
- **Estrutura de pastas reorganizada:**
  - `contiti.py` → `src/main.py` (renomeado e movido para diretório `src/`)
  - `yolov8n.pt` → `models/yolov8n.pt` (movido para diretório `models/`)

- **`src/main.py`** — Alterações em relação ao `contiti.py` original do `origin/main`:

  | Aspecto | Antes (`contiti.py`) | Depois (`src/main.py`) |
  |---|---|---|
  | Salvamento no Supabase | A cada frame (sem cooldown), travava o vídeo | **Cooldown de 3 segundos** entre inserções |
  | Caminho do modelo | `"yolov8n.pt"` (raiz, hardcoded) | `models/yolov8n.pt` via `os.path` dinâmico |
  | Log no terminal | `print` duplicado no mesmo `if` | Log diferenciado: "Salvando no banco..." vs apenas "Pessoas detectadas:" |
  | Código morto | `salvar_no_supabase` comentado, `os.system('cls')` comentado | Chamada ao Supabase ativa com controle de throttle |

- **`.gitignore`** — Atualizado com regras Python padrão (`__pycache__/`, `*.pyc`, `models/*.pt`).

---

### Removido

- **`registros_rows.sql`** — Dump de dados de teste do Supabase removido do repositório.

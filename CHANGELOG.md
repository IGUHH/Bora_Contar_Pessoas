# Changelog

Todas as alterações relevantes deste projeto serão documentadas neste arquivo.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [Unreleased] — Branch `refactor/otimize-request-supabase`

> Comparado com: `origin/main` (GitHub — https://github.com/IGUHH/Bora_Contar_Pessoas)

---

### Adicionado

- **`requirements.txt`** — Arquivo de dependências criado com os pacotes necessários (`ultralytics`, `opencv-python`, `supabase`, `python-dotenv`).
- **`CHANGELOG.md`** — Este arquivo de changelog do projeto.

---

### Alterado

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

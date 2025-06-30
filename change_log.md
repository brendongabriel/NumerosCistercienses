# 📋 CHANGELOG

## [v1.0.0] – 26/05/2025
### ✨ Adicionado
- `.gitignore` para ignorar arquivos temporários
- `requirements.txt` com dependências do projeto
- Geração de números Cistercienses em `generateNumber.py`
- Predição de números com modelo `.h5`
- Interface gráfica com `Tkinter` (`app.py`)
- Testes automatizados com `pytest` (`test_unit.py`)

### 🔁 Pull Requests
- PR #1: `chore/add-gitignore`
- PR #2: `test/add-unit-tests`

---

## [v1.1.0] – 01/07/2025
### ⚙️ Adicionado
- CI/CD com GitHub Actions
- Branches `qa` e `prd` para controle de ambientes
- Tag `v1.0.0` publicada
- Estrutura para documentação e auditoria de mudanças

### 🔁 Pull Requests
- PR #3: `ci: add GitHub Actions workflow`
- PR #4: `release: v1.0.0 → prd`

---

## [v1.1.1] – 29/06/2025

### 🐛 Corrigido
- Lançamento explícito de `FileNotFoundError` ao tentar carregar imagem inexistente na função `carregar_imagem_teste()`
- Correção garante que o teste `test_carregar_imagem_teste_invalida` passe com sucesso na pipeline do GitHub Actions

### 🔁 Pull Requests
- PR #5: `fix/file-not-found-error` → `qa`
- PR #6: `release: correção do erro de imagem inválida (v1.1.1)` → `prd`

### 🔗 Issues relacionadas
- Issue #3: `[Correção] Lançar FileNotFoundError ao carregar imagem inválida`

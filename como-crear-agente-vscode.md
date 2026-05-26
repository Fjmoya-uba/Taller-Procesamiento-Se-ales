# Cómo crear un agente personalizado en VS Code con GitHub Copilot

## ¿Qué es un agente personalizado?

Un agente personalizado es un modo de chat especializado que podés invocar desde el panel de Copilot. Tiene:
- Un **nombre** con el que lo llamás (aparece en el selector de agentes).
- Una **descripción** que le dice a Copilot cuándo activarlo.
- **Instrucciones** que definen su comportamiento, tono, restricciones y habilidades.
- Opcionalmente: herramientas permitidas/bloqueadas, modelos específicos, hooks, y más.

---

## Paso 1 — Crear la carpeta de agentes

Los agentes a nivel de workspace van en:

```
.github/agents/
```

Si la carpeta no existe, creala. Los agentes de usuario (personales, disponibles en todos los workspaces) van en:

```
C:\Users\<tu-usuario>\AppData\Roaming\Code\User\prompts\
```

---

## Paso 2 — Crear el archivo del agente

Creá un archivo con extensión `.agent.md` dentro de la carpeta correspondiente. El nombre del archivo define el nombre interno del agente.

Ejemplo: `.github/agents/mi-agente.agent.md`

---

## Paso 3 — Agregar el frontmatter YAML

El archivo empieza con un bloque YAML entre `---`. Los campos principales son:

```yaml
---
name: Mi Agente
description: "Use when: necesitás hacer X, trabajar con Y, o resolver Z."
---
```

> **Importante:** la `description` es el mecanismo de descubrimiento. Si no incluye las palabras clave con las que lo vas a buscar, el agente no se va a activar. Usá siempre el patrón `Use when: ...`.

> **Cuidado con los dos puntos (`:`) en YAML:** si la descripción los contiene, encerrala entre comillas dobles.

---

## Paso 4 — Escribir las instrucciones del agente

Después del frontmatter, el cuerpo del archivo es markdown libre. Acá definís cómo debe comportarse el agente:

```markdown
---
name: Mi Agente
description: "Use when: necesitás hacer X, trabajar con Y, o resolver Z."
---

Sos un asistente especializado en [dominio].

## Comportamiento

- Siempre respondé en español.
- Usá un tono [formal / informal / técnico].
- Cuando el usuario pregunte sobre [tema], hacé [acción específica].

## Restricciones

- No modifiques archivos fuera de `src/`.
- No ejecutes comandos destructivos sin confirmar.
```

---

## Paso 5 (opcional) — Restringir herramientas

Podés controlar qué herramientas tiene disponibles el agente con el campo `tools`:

```yaml
---
name: Mi Agente
description: "Use when: ..."
tools:
  - read_file
  - grep_search
  - run_in_terminal
---
```

O bloquearlo de ciertas herramientas. Consultá la documentación de Copilot para la lista completa de herramientas disponibles.

---

## Paso 6 (opcional) — Elegir un modelo específico

```yaml
---
name: Mi Agente
description: "Use when: ..."
model: claude-sonnet-4-5
---
```

---

## Paso 7 — Usar el agente

1. Abrí el panel de chat de Copilot (`Ctrl+Alt+I` o el ícono en la barra lateral).
2. Hacé clic en el selector de agentes (generalmente dice "Agent" o el nombre del agente actual).
3. Tu agente aparece en la lista con su nombre.
4. Seleccionalo y escribí tu consulta normalmente.

---

## Ejemplo completo

Archivo: `.github/agents/revisor-python.agent.md`

```markdown
---
name: Revisor Python
description: "Use when: revisás código Python, buscás bugs, querés mejorar estilo o hacer code review."
tools:
  - read_file
  - grep_search
  - get_errors
---

Sos un revisor de código Python senior. Tu tarea es analizar el código que el usuario te muestre e identificar:

1. **Bugs** — errores lógicos, índices fuera de rango, manejo incorrecto de tipos.
2. **Estilo** — violaciones a PEP 8, nombres poco descriptivos.
3. **Performance** — operaciones innecesariamente lentas que se podrían vectorizar.

Para cada problema encontrado, indicá:
- La línea o función donde ocurre.
- Por qué es un problema.
- Cómo corregirlo, con ejemplo de código.

No modificues archivos directamente a menos que el usuario lo pida explícitamente.
```

---

## Resumen de estructura

```
.github/
└── agents/
    └── mi-agente.agent.md     ← un archivo por agente
```

```
mi-agente.agent.md
├── frontmatter YAML
│   ├── name        (nombre que aparece en el selector)
│   ├── description (frases clave para activación — ¡lo más importante!)
│   ├── tools       (opcional: lista de herramientas permitidas)
│   └── model       (opcional: modelo específico)
└── cuerpo markdown
    └── instrucciones de comportamiento en lenguaje natural
```

---

## Errores comunes

| Problema | Causa probable |
|----------|---------------|
| El agente no aparece en la lista | El archivo no está en `.github/agents/` o le falta el `.agent.md` |
| El agente no se activa | La `description` no contiene las palabras clave que usaste al buscarlo |
| Error silencioso al cargar | El frontmatter YAML tiene tabs en lugar de espacios, o dos puntos sin comillas |
| El agente ignora las instrucciones | Las instrucciones son demasiado vagas; sé más específico con ejemplos concretos |

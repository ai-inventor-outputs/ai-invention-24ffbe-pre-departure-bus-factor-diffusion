# Candidate repo list: well-known real OSS repos, spanning >=3 star bands and
# >=4 language ecosystems. No claims are made here about founder dominance —
# that is measured empirically from cloned git history in build_dataset.py.
CANDIDATES = [
    # Python
    "pallets/flask", "psf/requests", "httpie/cli", "psf/black", "python/mypy",
    "python-poetry/poetry", "pallets/click", "tqdm/tqdm", "Textualize/rich",
    "Textualize/textual", "encode/httpx", "encode/uvicorn", "encode/starlette",
    "crsmithdev/arrow", "joke2k/faker", "amoffat/sh", "pyenv/pyenv",
    "pypa/pipenv", "benoitc/gunicorn", "kennethreitz/records", "jazzband/tablib",
    "cookiecutter/cookiecutter", "pydantic/pydantic", "tiangolo/typer",
    "urwid/urwid", "django-extensions/django-extensions",
    # JavaScript / TypeScript
    "expressjs/express", "lodash/lodash", "axios/axios", "chalk/chalk",
    "tj/commander.js", "yargs/yargs", "moment/moment", "iamkun/dayjs",
    "socketio/socket.io", "remy/nodemon", "Unitech/pm2", "avajs/ava",
    "preactjs/preact", "alpinejs/alpine", "bigskysoftware/htmx",
    "pmndrs/zustand", "pmndrs/valtio", "sindresorhus/got",
    "sindresorhus/ora", "sindresorhus/execa", "visionmedia/debug",
    "motdotla/dotenv", "expressjs/cors", "jaredhanson/passport",
    # Go
    "spf13/cobra", "spf13/viper", "gin-gonic/gin", "labstack/echo",
    "junegunn/fzf", "gohugoio/hugo", "jesseduffield/lazygit",
    "go-delve/delve", "cosmtrek/air", "99designs/gqlgen", "go-chi/chi",
    "urfave/cli", "spf13/afero", "gorilla/mux", "gorilla/websocket",
    # Ruby
    "sinatra/sinatra", "lostisland/faraday", "jnunemaker/httparty",
    "rails/thor", "rubocop/rubocop", "pry/pry", "guard/guard",
    "capistrano/capistrano", "jekyll/jekyll", "middleman/middleman",
    "carrierwaveuploader/carrierwave", "mperham/sidekiq",
    # Rust
    "BurntSushi/ripgrep", "sharkdp/bat", "sharkdp/fd", "eza-community/eza",
    "starship/starship", "XAMPPRocky/tokei", "sharkdp/hyperfine",
    "rust-lang/mdBook", "killercup/cargo-edit", "sharkdp/fd",
    "clap-rs/clap", "serde-rs/serde",
    # C / C++
    "nlohmann/json", "gabime/spdlog", "fmtlib/fmt",
    "catchorg/Catch2", "yhirose/cpp-httplib", "dropbox/json11",
    "libuv/libuv", "curl/curl", "antirez/redis",
    # Java
    "square/retrofit", "JakeWharton/butterknife", "google/gson",
    "jhy/jsoup", "brettwooldridge/HikariCP", "FasterXML/jackson-core",
]

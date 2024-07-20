FROM mcr.microsoft.com/devcontainers/python:3.12

USER root
COPY --from=docker:20.10 /usr/local/bin/docker /usr/local/bin/

USER vscode
WORKDIR /home/vscode
RUN pipx install poetry  &&  \
    pipx inject poetry "poetry-dynamic-versioning[plugin]"
FROM mcr.microsoft.com/vscode/devcontainers/python:3.6
COPY setup.sh ./
ARG USERNAME=vscode

RUN chmod +x setup.sh
RUN ./setup.sh

# Switch from root to user
USER $USERNAME

# Add user to video group to allow access to webcam and serial data group
RUN sudo usermod --append --groups video $USERNAME && \
    sudo gpasswd --add $USERNAME dialout && \
    sudo gpasswd --add $USERNAME plugdev
    
FROM node

RUN npm install -g http-server
ADD . /presentation

EXPOSE 8080

WORKDIR /presentation

ENTRYPOINT ["http-server"]
CMD [""]

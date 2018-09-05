FROM node:latest

EXPOSE 8080
WORKDIR /bindmount

COPY ./ ./

RUN npm install --no-progress --ignore-optional

CMD npm run start

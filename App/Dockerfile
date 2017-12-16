FROM node:latest
WORKDIR ./UserManager
ADD ./UserManager /UserManager
ENV PORT=3000
ENV DB_URL='mongodb://127.0.0.1:27017/alcDB'
EXPOSE ${PORT}
RUN npm install
CMD ["npm", "start"]

# Frontend Dockerfile
FROM node:18 as build-stage

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build --prod

# Nginx Stage
FROM nginx:alpine

RUN ls -larth
COPY --from=build-stage dist/house_filtering/browser /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

FROM node:16.17 as dependencies
WORKDIR /next
COPY package.json package-lock.json ./
RUN npm install --frozen-lockfile

FROM node:16.17 as builder
WORKDIR /next
COPY . .
COPY --from=dependencies /next/node_modules ./node_modules
RUN npm run build

FROM node:16.17 as runner
WORKDIR /next
ENV NODE_ENV production

COPY --from=builder /next/public ./public
COPY --from=builder /next/package.json ./package.json
COPY --from=builder /next/.next ./.next
COPY --from=builder /next/node_modules ./node_modules

EXPOSE 3000
CMD ["npm","run", "dev"]
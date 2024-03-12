#! /usr/bin/env node

import { createSocket } from "dgram";

const server = createSocket("udp4", (message, { address, port }) => {
  console.log(`${message}`);
  server.send([`${port}:`, message], port, address, (error) => {
    error && console.error(error);
    server.close();
  });
}).bind(20213, "127.0.0.1");

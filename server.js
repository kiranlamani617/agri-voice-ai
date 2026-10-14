// AgriVoice UI - Zero-dependency Node.js Production/Dev Server
// Runs on port 3000, serves static assets and proxies API calls to Django (port 8000)

const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = process.env.PORT || 3000;
const BACKEND_HOST = process.env.BACKEND_HOST || '127.0.0.1';
const BACKEND_PORT = process.env.BACKEND_PORT || 8000;

const MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav',
    '.woff2': 'font/woff2',
    '.woff': 'font/woff'
};

const server = http.createServer((req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const pathname = parsedUrl.pathname;

    // Enable CORS for development flexibility
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, X-Requested-With');

    if (req.method === 'OPTIONS') {
        res.writeHead(200);
        res.end();
        return;
    }

    // Proxy API requests to Django backend on port 8000
    if (pathname.startsWith('/api/') || pathname.startsWith('/auth/')) {
        const proxyOptions = {
            hostname: BACKEND_HOST,
            port: BACKEND_PORT,
            path: req.url,
            method: req.method,
            headers: {
                ...req.headers,
                host: `${BACKEND_HOST}:${BACKEND_PORT}`
            }
        };

        const proxyReq = http.request(proxyOptions, (proxyRes) => {
            res.writeHead(proxyRes.statusCode, proxyRes.headers);
            proxyRes.pipe(res);
        });

        proxyReq.on('error', (err) => {
            console.error(`Backend Proxy Error: ${err.message}`);
            res.writeHead(502, { 'Content-Type': 'application/json' });
            res.end(JSON.stringify({
                error: 'Backend API unreachable. Ensure Django server is running on port 8000.',
                detail: err.message
            }));
        });

        req.pipe(proxyReq);
        return;
    }

    // Serve static files from agrivoice-ui directory
    let filePath = path.join(__dirname, pathname === '/' ? 'index.html' : pathname);
    let extname = path.extname(filePath).toLowerCase();

    fs.stat(filePath, (err, stats) => {
        if (err || !stats.isFile()) {
            // SPA fallback to index.html if file not found
            filePath = path.join(__dirname, 'index.html');
            extname = '.html';
        }

        fs.readFile(filePath, (readErr, content) => {
            if (readErr) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end(`Internal Server Error: ${readErr.message}`);
                return;
            }

            const contentType = MIME_TYPES[extname] || 'application/octet-stream';
            res.writeHead(200, {
                'Content-Type': contentType,
                'Cache-Control': extname === '.html' ? 'no-cache' : 'public, max-age=3600'
            });
            res.end(content);
        });
    });
});

server.listen(PORT, () => {
    console.log(`🌾 AgriVoice UI running at http://localhost:${PORT}`);
    console.log(`🔌 Proxying API requests to http://${BACKEND_HOST}:${BACKEND_PORT}`);
});

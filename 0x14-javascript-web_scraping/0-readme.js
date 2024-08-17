#!/usr/bin/node
const fs = require('fs');
const path = require('path');

function readFile(filePath) {
	    try {
		            const content = fs.readFileSync(filePath, 'utf8');
		            console.log(content);
		        } catch (error) {
				        console.error(`Error occurred: ${error.message}`);
				    }
}

if (process.argv.length !== 3) {
	    console.log("Usage: node script.js <file_path>");
} else {
	    const filePath = path.resolve(process.argv[2]);
	    readFile(filePath);
}

import * as Os from 'node:os';
import * as remote from '@electron/remote';

// Globally export what OS we are on
const isLinux = process.platform === 'linux';
const isWin = process.platform === 'win32';
const isMac = process.platform === 'darwin';

// Show version numbers of bundled Electron.
window.addEventListener('DOMContentLoaded', () => {
	const replaceText = (selector: string, text: string) => {
		const element = document.getElementById(selector);
		if (element) {
			element.innerText = text;
		}
	};

	replaceText(`electron-version`, process.versions.electron);
	replaceText(`chrome-version`, process.versions.chrome);
	replaceText(`node-version`, process.versions.node);
	replaceText(`v8-version`, process.versions.v8);
});

// Get app version from package.json
const appVersion = remote.app.getVersion();

let osType;
if (isLinux) {
	osType = 'Linux';
} else if (isWin) {
	osType = 'Win';
} else if (isMac) {
	osType = 'MacOS';
} else {
	osType = 'BSD';
}

const archType = Os.arch();

// Show app version in about.html
window.addEventListener('DOMContentLoaded', () => {
	const replaceText = (selector: string, text: string) => {
		const element = document.getElementById(selector);
		if (element) {
			element.innerText = text;
		}
	};

	replaceText('caprine-version', appVersion);
	replaceText('os-type', osType);
	replaceText('arch-type', archType);
});

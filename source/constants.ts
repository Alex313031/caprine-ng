import * as path from 'node:path';
import {fixPathForAsarUnpack} from 'electron-util';

export const caprineIconPath = fixPathForAsarUnpack(path.join(__dirname, '..', 'static', 'Icon.png'));
export const caprineIcon64Path = fixPathForAsarUnpack(path.join(__dirname, '..', 'static', 'Icon64.png'));
export const caprineWinIconPath = fixPathForAsarUnpack(path.join(__dirname, '..', 'static', 'icon.ico'));

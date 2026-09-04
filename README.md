
# Kritabuddy
Add a desktop pet to your Krita panel!

## Download
To download Kritabuddy, go to https://github.com/autowattage/kritabuddy/releases/latest. For Krita users 6.0.0+, download kritabuddy6.zip, and for Krita users 5.0.0+, download kritabuddy5.zip.

Open Krita and navigate to <strong>Settings → Manage Resources → Open Resources</strong> and unzip kritabuddy.zip to the pykrita resource folder.

## Usage
To enable, go to <strong>Tools → Scripts → Toggle Kritabuddy</strong>.

Clicking the Kritabuddy hides it from view.

## Spinoff guide
The Kritabuddy folder structure looks like this:

- kritabuddy/
	- img/
		- idle.gif
		- sit.gif
		- walk-flipped.gif
		- walk.gif
	- \_\_init__.py
	- kritabuddy[]().py
	- manual.html
- kritabuddy.desktop

The kritabuddy/img/ folder contains gif files for the Kritabuddy animations. All the files inside must be gifs of the same dimensions.

kritabuddy[]().py contains two classes, character and kritabuddy. The character class creates a 'rig' that the kritabuddy can control and animate.

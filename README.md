# Instagram Spotify Bio Updater

This project allows you to automatically update your Instagram bio with the currently playing song from Spotify. It uses the Spotify API to fetch the current song and the Instagram API to update your bio.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Spotify Authentication](#spotify-authentication)
  - [Instagram Authentication](#instagram-authentication)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine.
- A Spotify account.
- An Instagram account.

## Getting Started

### Spotify Authentication

To use the Spotify API, you need to create a Spotify Developer account and set up an application to obtain your `CLIENT_ID`, `CLIENT_SECRET`, and `REDIRECT_URI`.

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on "Create an App".
4. Fill in the required details and agree to the terms.
5. Once the app is created, you will see your `CLIENT_ID` and `CLIENT_SECRET`.
6. Set the `Redirect URI` to `http://localhost:8888/callback` (or any other URI you prefer).
7. Make sure to add the necessary scopes for your application. For this project, you need:
   - `user-read-playback-state`
   - `user-read-currently-playing`

### Instagram Authentication

To update your Instagram bio, you need to authenticate your session and obtain the necessary cookies.

1. Log in to your Instagram account on a web browser.
2. Change your bio to trigger a request, and use a tool like [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) to capture the network request.
3. Look for the request to `https://www.instagram.com/api/v1/web/accounts/edit/` and copy the `Cookie` and `X-CSRFToken` values.
4. Replace the placeholders in your code with the actual values:
   - `XCsrftoken`
   - `COOKIE`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shibakek2/instagram-spotify-bio-changer.git
   cd instagram-spotify-bio-updater
   ```

2. Install the required packages:
   ```bash
   pip install spotipy requests
   ```

3. Update the `instagramspotify.py` file with your Spotify and Instagram credentials.

## Usage

1. Run the script:
   ```bash
   python instagramspotify.py
   ```

2. The script will continuously check for the currently playing song on Spotify and update your Instagram bio accordingly.

## Contributing

Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

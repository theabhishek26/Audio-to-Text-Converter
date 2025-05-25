# Audio-to-Text Converter Web App

A Flask web application that converts audio files (MP3, WAV, OGG, M4A) to text using AssemblyAI's speech-to-text API.

## Features

- 🎤 Upload audio files via drag & drop or file browser
- ✍️ Accurate speech-to-text conversion
- 📋 Copy results to clipboard with one click
- 📱 Responsive design works on all devices
- ⚡ Fast processing with progress indicators

## Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **APIs**: AssemblyAI Speech-to-Text
- **Dependencies**: See [requirements.txt](/requirements.txt)

## Prerequisites

- Python 3.7+
- AssemblyAI API key (free tier available)
- FFmpeg (for some audio formats)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/theabhishek26/Audio-to-Text-Converter.git
cd Audio-to-Text-Converter
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```env
AAI_API_KEY=your_assemblyai_api_key
```

5. Create uploads directory:
```bash
mkdir uploads
```

## Usage

1. Run the application:
```bash
python app.py
```

2. Open your browser to:
```
http://localhost:5000
```

3. Upload an audio file and wait for transcription

## Project Structure

```
Audio-to-Text-Converter/
├── app.py                # Main application file
├── static/               # Static files (CSS, JS)
├── templates/            # HTML templates
│   └── index.html        # Main interface
├── uploads/              # Audio file storage
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
└── README.md             # This file
```

## Configuration

Edit `app.py` to configure:
- File size limits
- Allowed file extensions
- Upload folder location

## Troubleshooting

**Error: Invalid API Key**
- Verify your AssemblyAI API key in `.env`

**Error: File Not Uploading**
- Check `uploads/` directory exists
- Verify file permissions

**Error: Transcription Failing**
- Ensure audio quality is good
- Check supported formats: MP3, WAV, OGG, M4A

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Abhishek - [@yourtwitter](https://gmail.com/) - abhishek26kashyap@gmail.com

Project Link: [https://github.com/theabhishek26/Audio-to-Text-Converter](https://github.com/theabhishek26/Audio-to-Text-Converter)
```

### How to add this to your project:

1. Create a new file named `README.md` in your project root
2. Paste the above content
3. Customize the sections marked with your information
4. Add a screenshot (optional but recommended)
5. Commit the file:
```bash
git add README.md
git commit -m "Add project README"
git push origin main
```
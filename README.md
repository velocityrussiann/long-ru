# 🇷🇺 Velocity Russian - Automated Content Generator

**Automated Russian learning content generator for YouTube**

Generates YouTube long-form videos with:
- ✅ AI-generated Russian phrases with English translations
- ✅ Professional text-to-speech (Edge TTS - SvetlanaNeural)
- ✅ Beautiful gradient backgrounds with text overlays
- ✅ Perfect audio-video synchronization
- ✅ Velocity Russian branding
- ✅ **NEVER repeats phrases** (permanent history tracking)

---

## 📅 Daily Schedule (American EST/EDT)

| Post | Time (EST) | Time (UTC) | Theme |
|------|------------|------------|-------|
| 1 | 9:00 AM | 14:00 UTC | Morning motivation |
| 2 | 12:00 PM | 17:00 UTC | Lunch break |
| 3 | 3:00 PM | 20:00 UTC | Afternoon pick-me-up |
| 4 | 7:00 PM | 00:00 UTC | Evening inspiration |

---

## 🎬 Available Categories (25 Total)

1. Motivation (Мотивация)
2. Love (Любовь)
3. Success (Успех)
4. Wisdom (Мудрость)
5. Happiness (Счастье)
6. Self Improvement (Самосовершенствование)
7. Gratitude (Благодарность)
8. Friendship (Дружба)
9. Hope (Надежда)
10. Creativity (Творчество)
11. Inner Peace (Внутренний покой)
12. Confidence (Уверенность)
13. Perseverance (Настойчивость)
14. Inspiration (Вдохновение)
15. Positive Life (Позитивная жизнь)
16. Courage (Смелость)
17. Kindness (Доброта)
18. Patience (Терпение)
19. Forgiveness (Прощение)
20. Strength (Сила)
21. Joy (Радость)
22. Balance (Баланс)
23. Growth (Рост)
24. Purpose (Цель)
25. Mindfulness (Осознанность)

---

## 🚀 GitHub Actions Setup

### Step 1: Add Secrets to GitHub Repository

Go to your GitHub repository → Settings → Secrets and variables → Actions

**Required Secrets:**

```bash
# Pollinations AI (for content generation)
POLLINATIONS_API_KEY=sk_your_api_key_here

# Facebook (for Reels upload)
FACEBOOK_ACCESS_TOKEN=your_token
FACEBOOK_PAGE_ID=your_page_id

# Instagram (for Reels upload)
INSTAGRAM_ACCESS_TOKEN=your_token
INSTAGRAM_ACCOUNT_ID=your_account_id

# Optional: Other platforms
VK_ACCESS_TOKEN=your_token
VK_GROUP_ID=your_group_id
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHANNEL_ID=your_channel_id
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_SECRET=your_secret
```

### Step 2: Enable GitHub Actions

1. Go to Actions tab in your GitHub repository
2. Enable workflows if disabled
3. The workflow will automatically run daily

### Step 3: Manual Testing

You can manually trigger the workflow:
1. Go to Actions → "Velocity Russian - Daily Long-Form Upload"
2. Click "Run workflow"
3. Select branch (main/master)
4. Click "Run workflow"

---

## 💻 Local Testing

### Prerequisites

```bash
# Install Python 3.11+
# Install FFmpeg
# Install dependencies
pip install -r requirements.txt
```

### Generate Single Long-Form Video

```bash
python youtube_longform_automation.py
```

### Generate with Specific Category

```bash
python youtube_longform_automation.py --category "Motivation"
```

### Generate with Specific Phrase Count

```bash
python youtube_longform_automation.py --phrases 120
```

### Upload to YouTube

```bash
python upload_to_youtube.py
```

---

## 📁 Project Structure

```
velocity Russian/
├── .env                              # API keys and credentials
├── .github/
│   └── workflows/
│       ├── youtube_longform_generator.yml  # Daily long-form generator
│       └── daily_4x_upload.yml       # Short-form upload workflow
├── youtube_longform_automation.py    # Main long-form video generator
├── generate_thumbnail.py             # AI thumbnail generator (gpt-image-2)
├── upload_to_youtube.py              # YouTube upload script
├── upload_all_platforms.py           # Multi-platform upload script
├── upload/
│   ├── upload_facebook.py
│   ├── upload_instagram.py
│   ├── upload_vk.py
│   └── ...
├── output/
│   ├── longform_videos/              # Generated YouTube videos
│   ├── video/                        # Generated short-form reels
│   ├── history/                      # Phrase history (NEVER delete!)
│   └── daily_summary_*.json         # Daily generation logs
└── requirements.txt
```

---

## 🔧 Configuration

### Timezone Adjustment

The workflow uses EST/EDT (UTC-5). To change timezone:

1. Edit `.github/workflows/daily_4x_upload.yml`
2. Modify cron schedules:
   ```yaml
   # For PST (UTC-8):
   - cron: '0 17 * * *'  # 9 AM PST
   - cron: '0 20 * * *'  # 12 PM PST
   - cron: '0 23 * * *'  # 3 PM PST
   - cron: '0 3 * * *'   # 7 PM PST
   ```

### Posting Frequency

To change from 4x to 3x daily:

1. Edit `.github/workflows/daily_4x_upload.yml`
2. Remove one cron schedule
3. Update `generate_daily_content(times_per_day=3)` in script

---

## 🎬 Video Specifications

- **Resolution:** 1080x1920 (9:16 vertical)
- **Format:** MP4 (H.264 + AAC)
- **Duration:** ~30-50 seconds (5 phrases)
- **Frame Rate:** 30 FPS
- **Audio:** Edge TTS (GuyNeural EN, SvetlanaNeural RU)

---

## 📊 Phrase History

All generated phrases are stored in:
```
output/history/all_generated_phrases.json
```

**This file is PERMANENT and should NEVER be deleted.**

It ensures:
- ✅ No phrase is ever repeated
- ✅ Fresh content every day
- ✅ Tracking of all generated content

---

## 🐛 Troubleshooting

### Video Generation Fails

```bash
# Check FFmpeg installation
ffmpeg -version

# Reinstall if needed
sudo apt-get install ffmpeg  # Linux
brew install ffmpeg          # macOS
```

### Audio Upload Fails

```bash
# Check .env file
cat .env | grep FACEBOOK
cat .env | grep INSTAGRAM

# Verify tokens are valid
# Regenerate if expired
```

### GitHub Actions Fails

1. Check Actions tab for error logs
2. Verify all secrets are set correctly
3. Check artifact uploads for generated files
4. Review logs for specific error messages

---

## 📈 Performance Metrics

- **Generation Time:** ~2-3 minutes per reel
- **Upload Time:** ~1-2 minutes per platform
- **Total Workflow:** ~5-10 minutes per post
- **Daily Capacity:** 4 posts × 5 phrases = 20 phrases/day
- **Category Rotation:** 25 categories = 6+ days before repeat

---

## 🎯 Key Features

### ✅ Perfect Audio-Video Sync
- Each image displays for exact audio duration
- English + 500ms pause + Russian timing preserved
- No early transitions or cut-offs

### ✅ Natural Speech
- Phrases include commas for breathing room
- Example: "Dream big, start small"
- TTS sounds natural, not robotic

### ✅ Professional Design
- Multi-stop gradient backgrounds
- Distinct colors: Navy (EN) / Light Purple (RU) / Peach (Pronunciation)
- Velocity Russian branding on every frame

### ✅ Never Repeats
- Permanent phrase history tracking
- AI generates fresh content every time
- Checks all phrases before generation

---

## 📞 Support

For issues or questions:
1. Check GitHub Actions logs
2. Review error messages in output
3. Verify all API credentials
4. Check phrase history for duplicates

---

## 📄 License

This project is for educational purposes. Respect platform API terms of service.

---

**Made with ❤️ for Russian learners worldwide**

🇷🇺 Learn Russian with Velocity Russian! 🇷🇺

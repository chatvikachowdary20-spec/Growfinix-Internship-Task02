# AI-Powered Data Extraction (Unstructured to JSON)

## Overview
This project extracts structured information from unstructured customer emails using the OpenAI API.

## Features
- Extract customer name
- Extract requested travel dates
- Extract destination
- Save results as JSON

## Technologies Used
- Python
- OpenAI API
- JSON

## Input Example

Hello Team,

My name is Rahul Sharma.

I am planning a vacation to Bali with my family. We would like to travel from 10 August 2026 to 15 August 2026.

Please share hotel and package details.

Thank you,
Rahul Sharma

## Output

```json
{
  "customer_name": "Rahul Sharma",
  "requested_dates": "10 August 2026 to 15 August 2026",
  "destination": "Bali"
}
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

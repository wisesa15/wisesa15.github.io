To do:

1. bikin feature discount
2. bikin LLM-based chat hitting on Gemini API (the only one that gives you free API)
3. ganti tabel jadi UI lain yang bisa ngasih fleksibilitas ketika tampilannya itu mobile. Jadi dia bisa kebawah dibandingkan tetep ke samping kayak yang sekarang.

# Format json nanti ketika butuh ekstrak dari LLM

{
"people": ["Priyo", "Rakha", "Nopa", "Lukas"],
"expenses": [
{
"payer": "Lukas",
"amount": 70000,
"description": "Billiard",
"distribution": {
"Priyo": 1,
"Rakha": 1,
"Nopa": 1,
"Lukas": 1
}
},
{
"payer": "Lukas",
"amount": 84000,
"description": "Food",
"distribution": {
"Rakha": 1,
"Lukas": 1
}
},
{
"payer": "Rakha",
"amount": 68000,
"discount": 5000,
"description": "Coffee",
"distribution": {
"Priyo": 20000,
"Lukas": 24000,
"Rakha": 24000
},
"equal_discount": true
}
]
}

{
"people": ["Priyo", "Rakha", "Nopa", "Lukas"],
"expenses": [
{
"payer": "Lukas",
"amount": 70000,
"description": "Billiard",
"distribution": {
"Priyo": 1,
"Rakha": 1,
"Nopa": 1,
"Lukas": 1
}
},
{
"payer": "Lukas",
"amount": 84000,
"description": "Food",
"distribution": {
"Rakha": 1,
"Lukas": 1
}
},
{
"payer": "Rakha",
"amount": 68000,
"discount": 5000,
"description": "Coffee",
"distribution": {
"Priyo": 20000,
"Lukas": 24000,
"Rakha": 24000
}
}
]
}

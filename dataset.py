TRAINING_DATA = [
 ("I want to make a flight from Moscow to Chicago on 21st September 2024", {
        "entities": [
            (24, 35, "From"),  # "Moscow"
            (36, 46, "To"),    # "Chicago"
            (47, 67, "Datetime")  # "21st September 2024"
        ]
    }),
    ("Book a flight from Berlin to New York on 15th October 2024", {
        "entities": [
            (14, 25, "From"),  # "Berlin"
            (26, 37, "To"),    # "New York"
            (38, 56, "Datetime")  # "15th October 2024"
        ]
    }),
    ("I need a ticket from Paris to Tokyo on 5th November 2024", {
        "entities": [
            (16, 26, "From"),  # "Paris"
            (27, 35, "To"),    # "Tokyo"
            (36, 55, "Datetime")  # "5th November 2024"
        ]
    }),
    ("Schedule my flight from London to Sydney on 10th December 2024", {
        "entities": [
            (19, 30, "From"),  # "London"
            (31, 40, "To"),    # "Sydney"
            (41, 60, "Datetime")  # "10th December 2024"
        ]
    }),
    ("I want to fly from Madrid to Los Angeles on 1st January 2025", {
        "entities": [
            (14, 25, "From"),  # "Madrid"
            (26, 40, "To"),    # "Los Angeles"
            (41, 58, "Datetime")  # "1st January 2025"
        ]
    }),
    ("Book a ticket from Rome to Dubai on 20th February 2025", {
        "entities": [
            (16, 25, "From"),  # "Rome"
            (26, 34, "To"),    # "Dubai"
            (35, 53, "Datetime")  # "20th February 2025"
        ]
    }),
    ("I need a flight from Amsterdam to Bangkok on 15th March 2025", {
        "entities": [
            (16, 30, "From"),  # "Amsterdam"
            (31, 41, "To"),    # "Bangkok"
            (41, 56, "Datetime")  # "15th March 2025"
        ]
    }),
    ("Schedule a flight from Vienna to Hong Kong on 25th April 2025", {
        "entities": [
            (18, 29, "From"),  # "Vienna"
            (30, 43, "To"),    # "Hong Kong"
            (44, 60, "Datetime")  # "25th April 2025"
        ]
    }),
    ("I want to book a flight from Lisbon to Toronto on 10th May 2025", {
        "entities": [
            (24, 35, "From"),  # "Lisbon"
            (36, 46, "To"),    # "Toronto"
            (47, 59, "Datetime")  # "10th May 2025"
        ]
    }),
    ("Book my flight from beautiful Zurich to San Francisco on 30th June 2025", {
        "entities": [
            (15, 36, "From"),  # "Zurich"
            (27, 43, "To"),    # "San Francisco"
            (44, 61, "Datetime")  # "30th June 2025"
        ]
    }),
    ("I need a ticket from Brussels to Seoul on 15th July 2025", {
        "entities": [
            (16, 29, "From"),  # "Brussels"
            (30, 38, "To"),    # "Seoul"
            (39, 56, "Datetime")  # "15th July 2025"
        ]
    })
]
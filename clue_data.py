# clue_data.py

# Themes and word lists
THEMES = {
    "animals": [
        "elephant", "tiger", "kangaroo", "penguin", "dolphin",
        "giraffe", "octopus", "crocodile", "panda", "wolf"
    ],
    "fruits": [
        "apple", "banana", "cherry", "grape", "pineapple",
        "mango", "strawberry", "blueberry", "watermelon", "peach"
    ],
    "countries": [
        "france", "brazil", "canada", "japan", "germany",
        "italy", "russia", "mexico", "india", "egypt"
    ],
    "instruments": [
        "guitar", "piano", "violin", "drums", "flute",
        "saxophone", "trumpet", "harp", "cello", "clarinet"
    ],
    "planets": [
        "mercury", "venus", "earth", "mars", "jupiter",
        "saturn", "uranus", "neptune", "pluto", "ceres"
    ],
    "colors": [
        "red", "blue", "green", "yellow", "purple",
        "orange", "pink", "brown", "black", "white"
    ],
    "sports": [
        "soccer", "basketball", "tennis", "baseball", "golf",
        "boxing", "cricket", "swimming", "cycling", "volleyball"
    ],
    "jobs": [
        "teacher", "doctor", "engineer", "chef", "artist",
        "pilot", "nurse", "firefighter", "police", "musician"
    ],
    "vehicles": [
        "car", "bicycle", "airplane", "train", "boat",
        "motorcycle", "bus", "helicopter", "submarine", "truck"
    ],
    "mythology": [
        "zeus", "odin", "anubis", "poseidon", "hades",
        "thor", "ares", "isis", "kraken", "phoenix"
    ],
    "technology": [
        "computer", "smartphone", "robot", "drone", "satellite",
        "internet", "server", "algorithm", "database", "chip"
    ],
    "languages": [
        "english", "spanish", "french", "mandarin", "arabic",
        "hindi", "russian", "portuguese", "japanese", "german"
    ],
    # New themes:
    "food": [
        "pizza", "burger", "sushi", "taco", "pasta",
        "salad", "steak", "chocolate", "ice cream", "sandwich"
    ],
    "movies": [
        "inception", "titanic", "avatar", "gladiator", "matrix",
        "jaws", "star wars", "godfather", "rocky", "casablanca"
    ],
    "video_games": [
        "mario", "zelda", "minecraft", "doom", "fortnite",
        "tetris", "halo", "pac-man", "sonic", "counter-strike"
    ],
    "literature": [
        "hamlet", "1984", "dune", "gatsby", "moby dick",
        "frankenstein", "pride", "prejudice", "crime", "punishment"
    ],
    "tv_shows": ["friends", "breaking bad", "the office", "game of thrones", "stranger things"],
    "historical_figures": ["einstein", "cleopatra", "lincoln", "gandhi", "napoleon"],
    "comics": ["batman", "superman", "spiderman", "wolverine", "iron man", "deadpool", "hulk", "wonder woman", "flash", "aquaman"],
    "famous_landmarks": ["eiffel tower", "great wall", "pyramids", "statue of liberty", "colosseum", "taj mahal", "big ben", "sydney opera house", "christ the redeemer", "machu picchu"],
    "music_genres": ["rock", "pop", "jazz", "classical", "hip-hop", "electronic", "country", "blues", "reggae", "metal"],
    "cartoons": ["spongebob", "tom and jerry", "looney tunes", "rick and morty", "simpsons", "futurama", "adventure time", "regular show", "powerpuff girls", "peppa pig"],
}
# Theme-based background tint colors (light gradients)
THEME_COLORS = {
    "animals": ("#e9fce9", "#c2f0c2"),
    "fruits": ("#fff0f5", "#ffd1dc"),
    "countries": ("#e0f7fa", "#b2ebf2"),
    "instruments": ("#f3e5f5", "#d1c4e9"),
    "planets": ("#e3f2fd", "#bbdefb"),
    "colors": ("#f9fbe7", "#f0f4c3"),
    "sports": ("#fbe9e7", "#ffccbc"),
    "jobs": ("#f1f8e9", "#dcedc8"),
    "vehicles": ("#f0f4f8", "#cfd8dc"),
    "mythology": ("#fff3e0", "#ffe0b2"),
    "technology": ("#ede7f6", "#d1c4e9"),
    "languages": ("#e8f5e9", "#c8e6c9"),
    "food": ("#fffde7", "#fff9c4"),
    "movies": ("#efebe9", "#d7ccc8"),
    "video_games": ("#fce4ec", "#f8bbd0"),
    "literature": ("#e0f2f1", "#b2dfdb"),
    "tv_shows": ("#ede7f6", "#d1c4e9"),
    "historical_figures": ("#fff8e1", "#ffecb3"),
    "comics": ("#f3e5f5", "#e1bee7"),
    "famous_landmarks": ("#e1f5fe", "#b3e5fc"),
    "music_genres": ("#f1f8e9", "#dcedc8"),
    "cartoons": ("#fff3e0", "#ffe0b2"),
}
# Clues dictionary with three unique vague and helpful clues per word.
CLUES = {
    # Animals
    "elephant": {
        "vague": [
            "A massive creature roaming vast lands.",
            "Often pictured as a gentle giant of the wild.",
            "A symbol of memory and ancient wisdom."
        ],
        "helpful": [
            "It has a long trunk and large, flapping ears.",
            "Famous for its impressive size and tusks.",
            "Its social herds and iconic features set it apart."
        ]
    },
    "tiger": {
        "vague": [
            "A stealthy feline that stalks in the shadows.",
            "Often depicted in legends of power and mystery.",
            "A solitary creature with an enigmatic allure."
        ],
        "helpful": [
            "It sports bold stripes and a lithe frame.",
            "A native of dense jungles with piercing eyes.",
            "Its distinctive coat and fierce nature are well-known."
        ]
    },
    "kangaroo": {
        "vague": [
            "A bouncy creature from a faraway land.",
            "Often linked to wide, open terrains and unique hops.",
            "A marsupial known more by its silhouette than details."
        ],
        "helpful": [
            "It carries its young in a pouch with care.",
            "Noted for its powerful hind legs and unique gait.",
            "A classic emblem of distant, sunburnt landscapes."
        ]
    },
    "penguin": {
        "vague": [
            "A flightless bird with a quirky, waddling walk.",
            "Often envisioned in icy, remote settings.",
            "A creature that dresses in nature’s own tuxedo."
        ],
        "helpful": [
            "It thrives in frigid climates and icy waters.",
            "Recognized for its social nature and distinct gait.",
            "Its black-and-white appearance is unmistakable."
        ]
    },
    "dolphin": {
        "vague": [
            "A sleek marine dweller with a playful edge.",
            "Often seen as a symbol of intelligence in the sea.",
            "A creature that glides gracefully through the waves."
        ],
        "helpful": [
            "It uses echolocation to navigate underwater.",
            "Famous for its acrobatic leaps and friendly behavior.",
            "Its streamlined body is built for swift swimming."
        ]
    },
    "giraffe": {
        "vague": [
            "A towering creature with a uniquely elongated form.",
            "Often associated with sunlit savannas and treetops.",
            "A gentle giant that stands out from the herd."
        ],
        "helpful": [
            "It uses its height to reach leaves high in trees.",
            "Known for its patchy coat and graceful stride.",
            "Its long neck is one of its most defining features."
        ]
    },
    "octopus": {
        "vague": [
            "A mysterious denizen of the deep blue.",
            "Often shrouded in tales of ink and escape.",
            "A shape-shifting creature with fluid movements."
        ],
        "helpful": [
            "It possesses eight arms and an agile body.",
            "Notable for its ability to camouflage in an instant.",
            "Its ink defense mechanism is a natural marvel."
        ]
    },
    "crocodile": {
        "vague": [
            "A stealthy reptile lurking in murky waters.",
            "Often thought of as a relic from prehistoric times.",
            "A creature that blends silently into its swampy home."
        ],
        "helpful": [
            "It has a powerful bite armed with sharp teeth.",
            "Known for its armored skin and ambush tactics.",
            "Its cold-blooded nature makes it a formidable hunter."
        ]
    },
    "panda": {
        "vague": [
            "A fuzzy creature with a penchant for bamboo.",
            "Often seen as a cuddly symbol of conservation.",
            "A rare and gentle animal with a monochrome look."
        ],
        "helpful": [
            "It primarily feeds on bamboo in its natural habitat.",
            "Noted for its slow, deliberate movements and charm.",
            "Its distinctive black-and-white fur is iconic."
        ]
    },
    "wolf": {
        "vague": [
            "A wild creature known to roam in tight-knit groups.",
            "Often wrapped in legends of loyalty and mystery.",
            "A shadowy figure of the untamed wilderness."
        ],
        "helpful": [
            "It has keen senses and a powerful howl.",
            "Known for its strong pack dynamics and hunting skills.",
            "Its elusive nature and survival tactics are renowned."
        ]
    },

    # Fruits
    "apple": {
        "vague": [
            "A common fruit that hides a world of symbolism.",
            "Often seen as a crisp and familiar treat.",
            "A round fruit with a hint of the forbidden."
        ],
        "helpful": [
            "It is crisp, juicy, and comes in red or green.",
            "A symbol of health that features in many tales.",
            "Its simple shape and sweet taste are well-known."
        ]
    },
    "banana": {
        "vague": [
            "A curvy fruit with a tropical mystery.",
            "Often associated with a carefree, sunny vibe.",
            "A long, yellow treat that’s as playful as it seems."
        ],
        "helpful": [
            "It has a peel that must be removed to enjoy its flesh.",
            "Known for its sweet, soft texture and distinctive curve.",
            "Its vibrant color and tropical origin are unmistakable."
        ]
    },
    "cherry": {
        "vague": [
            "A tiny fruit that packs a secret punch.",
            "Often regarded as a delicate morsel of nature.",
            "A small red dot in a world of flavors."
        ],
        "helpful": [
            "It typically grows in pairs and adds a burst of tartness.",
            "Noted for its bright hue and jewel-like appearance.",
            "Its flavor is both sweet and a touch tangy."
        ]
    },
    "grape": {
        "vague": [
            "A small orb that clusters like hidden treasures.",
            "Often evoking images of vineyards and summer days.",
            "A diminutive fruit that comes in tight bunches."
        ],
        "helpful": [
            "It is juicy and can be eaten fresh or dried into raisins.",
            "Known for its sweetness and use in winemaking.",
            "Its delicate skin and burst of flavor are classic."
        ]
    },
    "pineapple": {
        "vague": [
            "A spiky tropical enigma with a sweet secret.",
            "Often seen as an exotic burst of flavor.",
            "A rough exterior that guards a luscious heart."
        ],
        "helpful": [
            "It has a fibrous exterior with juicy, tangy flesh.",
            "Known for its crown-like top and unique taste.",
            "Its blend of sweet and tart notes makes it stand out."
        ]
    },
    "mango": {
        "vague": [
            "A luscious tropical fruit that hints at paradise.",
            "Often evoking warm, sun-drenched memories.",
            "A soft, juicy treat wrapped in mystery."
        ],
        "helpful": [
            "It has a large pit and richly sweet, fragrant flesh.",
            "Famous for its smooth texture and vibrant color.",
            "Its tropical taste and aroma are hard to forget."
        ]
    },
    "strawberry": {
        "vague": [
            "A small red fruit that seems to whisper sweetness.",
            "Often associated with summer picnics and gentle charm.",
            "A heart-shaped delight that hints at freshness."
        ],
        "helpful": [
            "It sports tiny seeds on its surface and a juicy core.",
            "Known for its blend of sweetness with a hint of tartness.",
            "Its familiar red hue and delicate flavor are beloved."
        ]
    },
    "blueberry": {
        "vague": [
            "A petite, mysterious orb with a deep hue.",
            "Often seen as nature’s tiny, blue jewel.",
            "A small fruit that bursts with understated charm."
        ],
        "helpful": [
            "It is rich in antioxidants and subtle in sweetness.",
            "Commonly used in desserts and smoothies for its flavor.",
            "Its deep blue color and soft texture are distinctive."
        ]
    },
    "watermelon": {
        "vague": [
            "A colossal fruit synonymous with summer fun.",
            "Often evoking images of picnics and cooling refreshment.",
            "A green-skinned enigma hiding a scarlet secret."
        ],
        "helpful": [
            "It has a thick rind with juicy, red flesh inside.",
            "Known for its high water content and refreshing bite.",
            "Its striking contrast of colors makes it unmistakable."
        ]
    },
    "peach": {
        "vague": [
            "A fuzzy fruit that exudes a gentle sweetness.",
            "Often linked to warm, lazy summer afternoons.",
            "A soft, blushing fruit with a tender secret."
        ],
        "helpful": [
            "It has a delicate texture and a central pit.",
            "Known for its fragrant aroma and tender bite.",
            "Its unique blend of softness and tang is memorable."
        ]
    },

    # Countries
    "france": {
        "vague": [
            "A European nation wrapped in art and romance.",
            "Often imagined as a land of elegant mystery.",
            "A country where history and style merge effortlessly."
        ],
        "helpful": [
            "It is famed for its cuisine, wine, and iconic landmarks.",
            "Home to timeless symbols like the Eiffel Tower.",
            "Its cultural allure and artistic heritage are celebrated."
        ]
    },
    "brazil": {
        "vague": [
            "A vast land pulsing with rhythm and color.",
            "Often conjuring images of lush rainforests and festivals.",
            "A nation where nature and passion dance together."
        ],
        "helpful": [
            "It boasts vibrant traditions like Carnival and football.",
            "Known for its diverse landscapes and spirited culture.",
            "Its natural wonders and festive energy are renowned."
        ]
    },
    "canada": {
        "vague": [
            "A sprawling land of natural beauty and cool vibes.",
            "Often envisioned as a mosaic of wilderness and modernity.",
            "A country that whispers of snowy peaks and green forests."
        ],
        "helpful": [
            "It is known for its maple leaf and friendly communities.",
            "Famous for its breathtaking landscapes and outdoor lifestyle.",
            "Its blend of nature and urban charm appeals widely."
        ]
    },
    "japan": {
        "vague": [
            "A land where ancient tradition meets futuristic dreams.",
            "Often seen as a delicate balance of old and new.",
            "A country with quiet rituals and vibrant innovation."
        ],
        "helpful": [
            "It is celebrated for its art, cuisine, and cultural finesse.",
            "Home to time-honored practices like tea ceremonies.",
            "Its unique blend of history and modernity enchants many."
        ]
    },
    "germany": {
        "vague": [
            "A European country with a legacy of precision and lore.",
            "Often associated with robust industry and rich heritage.",
            "A nation where modernity meets storied traditions."
        ],
        "helpful": [
            "It is renowned for its engineering, beer, and castles.",
            "Famous for contributions to music, philosophy, and art.",
            "Its blend of tradition and innovation is widely respected."
        ]
    },
    "italy": {
        "vague": [
            "A country steeped in timeless art and flavor.",
            "Often conjuring images of cobbled streets and ancient ruins.",
            "A land where culinary and cultural tales unfold."
        ],
        "helpful": [
            "It is famous for its pasta, pizza, and historical marvels.",
            "Home to the Renaissance and eternal landmarks.",
            "Its rich culture and cuisine make it a global icon."
        ]
    },
    "russia": {
        "vague": [
            "A vast nation draped in wintry mystery.",
            "Often portrayed as both rugged and poetic.",
            "A land where cold landscapes meet epic legends."
        ],
        "helpful": [
            "It is known for its literature, ballet, and icy expanses.",
            "A country of contrasts, from vibrant cities to frozen tundras.",
            "Its cultural and historical impact resonates worldwide."
        ]
    },
    "mexico": {
        "vague": [
            "A country of vivid colors and enduring traditions.",
            "Often remembered for its lively festivals and heritage.",
            "A land where ancient ruins meet modern rhythms."
        ],
        "helpful": [
            "It is known for its rich cuisine, music, and history.",
            "Famous for its spicy flavors and warm hospitality.",
            "Its cultural mosaic and vibrant celebrations are renowned."
        ]
    },
    "india": {
        "vague": [
            "A land of endless contrasts and ancient tales.",
            "Often associated with vibrant chaos and mystique.",
            "A country where tradition and modernity coexist."
        ],
        "helpful": [
            "It is celebrated for its spices, festivals, and cinema.",
            "Home to diverse cultures and timeless traditions.",
            "Its rich heritage and dynamic growth captivate many."
        ]
    },
    "egypt": {
        "vague": [
            "An ancient land filled with timeless secrets.",
            "Often shrouded in myths of pharaohs and pyramids.",
            "A country where history and legend intertwine."
        ],
        "helpful": [
            "It is known for its monumental pyramids and the Nile.",
            "Famous for its ancient artifacts and storied past.",
            "Its archaeological wonders continue to fascinate the world."
        ]
    },

    # Instruments
    "guitar": {
        "vague": [
            "A string instrument that hums with rustic charm.",
            "Often seen as the soul of campfire ballads.",
            "A tool for strumming memories into melody."
        ],
        "helpful": [
            "It typically features six strings and a wooden body.",
            "Favored for its versatility across many music genres.",
            "Its sound is produced by plucking or strumming the strings."
        ]
    },
    "piano": {
        "vague": [
            "A keyboard instrument that resonates with elegance.",
            "Often envisioned as the heart of classical tunes.",
            "A grand presence in the world of harmony."
        ],
        "helpful": [
            "It has black and white keys that create a range of sounds.",
            "Played by striking keys to produce layered chords.",
            "Its dynamic range makes it a favorite in many genres."
        ]
    },
    "violin": {
        "vague": [
            "A small string instrument with a soulful cry.",
            "Often associated with delicate, emotional melodies.",
            "A slender instrument that sings with passion."
        ],
        "helpful": [
            "It is played with a bow to produce a haunting tone.",
            "Known for its expressive vibrato and rich timbre.",
            "Its portability and charm make it a classic choice."
        ]
    },
    "drums": {
        "vague": [
            "A rhythmic instrument that echoes deep beats.",
            "Often found setting the pace in lively gatherings.",
            "A percussive heartbeat in the realm of music."
        ],
        "helpful": [
            "It is played by striking surfaces with sticks or hands.",
            "Known for creating the foundational rhythm in music.",
            "Its dynamic sounds drive the tempo and energy of a song."
        ]
    },
    "flute": {
        "vague": [
            "A slender woodwind that whispers light melodies.",
            "Often associated with airy tunes and soft echoes.",
            "A simple instrument that floats in the soundscape."
        ],
        "helpful": [
            "It is played by blowing across an opening to create sound.",
            "Known for its clear, high-pitched tone.",
            "Its gentle timbre makes it a subtle musical voice."
        ]
    },
    "saxophone": {
        "vague": [
            "A curvy brass instrument with a soulful vibe.",
            "Often linked to smooth jazz and late-night moods.",
            "A musical tool that exudes cool and emotion."
        ],
        "helpful": [
            "It produces sound through a single-reed mouthpiece.",
            "Renowned for its warm, expressive tone.",
            "Its unique design contributes to a distinctive, jazzy sound."
        ]
    },
    "trumpet": {
        "vague": [
            "A compact brass instrument with a bold flair.",
            "Often heard in fanfares and energetic anthems.",
            "A small powerhouse in the realm of brass."
        ],
        "helpful": [
            "It is played by blowing into a cup-shaped mouthpiece.",
            "Known for its bright, piercing tone in ensembles.",
            "Its commanding sound stands out in any musical setting."
        ]
    },
    "harp": {
        "vague": [
            "A majestic string instrument with a dreamy aura.",
            "Often associated with legends and ethereal tunes.",
            "A large, graceful instrument that evokes calm."
        ],
        "helpful": [
            "It is played by plucking strings with delicate fingers.",
            "Known for its rich, resonant sound and elegant design.",
            "Its gentle chords create a serene musical backdrop."
        ]
    },
    "cello": {
        "vague": [
            "A deep, resonant string instrument with a somber tone.",
            "Often seen as the voice of melancholy in music.",
            "A large instrument that exudes warm, rich notes."
        ],
        "helpful": [
            "It is played with a bow to create a deep, velvety sound.",
            "Renowned for its rich timbre in orchestral pieces.",
            "Its lower registers add depth and emotion to music."
        ]
    },
    "clarinet": {
        "vague": [
            "A woodwind instrument with a soft, fluid character.",
            "Often heard weaving subtle melodies in ensembles.",
            "A slender instrument that offers a gentle whisper."
        ],
        "helpful": [
            "It uses a reed to generate a smooth, mellow sound.",
            "Known for its versatility in both classical and jazz settings.",
            "Its agile response makes it a favorite for intricate tunes."
        ]
    },

    # Planets
    "mercury": {
        "vague": [
            "A small, scorched world closest to the sun.",
            "Often depicted as a swift, rocky wanderer.",
            "A celestial body with extreme contrasts in temperature."
        ],
        "helpful": [
            "It has a cratered surface and negligible atmosphere.",
            "Its rapid orbit makes it one of the fastest planets.",
            "Its proximity to the sun results in dramatic heat swings."
        ]
    },
    "venus": {
        "vague": [
            "A bright, enigmatic planet cloaked in clouds.",
            "Often shrouded in a mysterious, golden glow.",
            "A world that remains hidden behind thick veils."
        ],
        "helpful": [
            "It is enveloped by dense, reflective clouds.",
            "Known for its extreme greenhouse conditions.",
            "Its surface remains obscured by a constant, toxic haze."
        ]
    },
    "earth": {
        "vague": [
            "Our blue home teeming with life and mystery.",
            "A vibrant orb of water and land in the cosmos.",
            "A unique planet where nature thrives in abundance."
        ],
        "helpful": [
            "It supports a diverse array of ecosystems and climates.",
            "Its oceans, continents, and atmosphere create a balanced home.",
            "Its life-sustaining features make it singular in our solar system."
        ]
    },
    "mars": {
        "vague": [
            "A ruddy world that sparks dreams of exploration.",
            "Often seen as a dusty, ancient relic of space.",
            "A barren landscape that hints at long-lost water flows."
        ],
        "helpful": [
            "It is renowned for its red hue and rocky surface.",
            "Often called the 'Red Planet' due to its color.",
            "Its terrain shows evidence of ancient riverbeds."
        ]
    },
    "jupiter": {
        "vague": [
            "A colossal gas giant dominating the night sky.",
            "Often depicted as a swirling, majestic orb.",
            "A giant that commands attention with its stormy presence."
        ],
        "helpful": [
            "It is the largest planet with a famous, long-lasting storm.",
            "Known for its numerous moons and turbulent atmosphere.",
            "Its massive size makes it a gravitational anchor in the solar system."
        ]
    },
    "saturn": {
        "vague": [
            "A regal gas giant adorned with stunning rings.",
            "Often celebrated for its elegant, banded appearance.",
            "A celestial wonder that enchants with its orbiting bands."
        ],
        "helpful": [
            "It boasts a spectacular ring system made of ice and rock.",
            "Famous for its array of moons and striking visual features.",
            "Its rings and gentle hues make it an icon of beauty."
        ]
    },
    "uranus": {
        "vague": [
            "A distant, tilted world with an offbeat spin.",
            "Often seen as mysterious due to its unusual axis.",
            "A chilly planet with a sideways glance at the stars."
        ],
        "helpful": [
            "It rotates on its side, creating extreme seasonal shifts.",
            "Known for its subtle rings and pale blue tint.",
            "Its unconventional tilt sets it apart from its neighbors."
        ]
    },
    "neptune": {
        "vague": [
            "A deep blue world swirling with icy mysteries.",
            "Often depicted as a remote, stormy giant.",
            "A planet that exudes a cold, mesmerizing charm."
        ],
        "helpful": [
            "It is celebrated for its intense blue color and windy storms.",
            "Famous for its dynamic weather patterns far from the sun.",
            "Its vivid hues and turbulent atmosphere make it unique."
        ]
    },
    "pluto": {
        "vague": [
            "A tiny, icy wanderer at the edge of the known.",
            "Often regarded as a mysterious outlier of the solar system.",
            "A cold, distant world that defies simple classification."
        ],
        "helpful": [
            "It was once considered the ninth planet before reclassification.",
            "Noted for its diminutive size and remote orbit.",
            "Its status as a dwarf planet remains a topic of debate."
        ]
    },
    "ceres": {
        "vague": [
            "A modest body nestled in the asteroid belt.",
            "Often seen as a bridge between planets and rocks.",
            "A small orb that quietly orbits among space debris."
        ],
        "helpful": [
            "It is the largest object in the asteroid belt.",
            "Known for its unique features that blur planetary lines.",
            "Its rocky surface and position spark curiosity among astronomers."
        ]
    },

    # Colors
    "red": {
        "vague": [
            "A bold hue that demands attention without words.",
            "Often associated with passion, danger, and energy.",
            "A striking color that leaves a lasting impression."
        ],
        "helpful": [
            "It is one of the primary colors, vibrant and intense.",
            "Often used to symbolize strong emotions or warnings.",
            "Its prominence in nature and art makes it unforgettable."
        ]
    },
    "blue": {
        "vague": [
            "A cool shade that soothes and intrigues the eye.",
            "Often linked to endless skies and deep oceans.",
            "A color that quietly evokes calm and mystery."
        ],
        "helpful": [
            "It is a primary color known for its serene qualities.",
            "Commonly used to represent depth and stability.",
            "Its soft, calming nature is found in many natural scenes."
        ]
    },
    "green": {
        "vague": [
            "A color that whispers of nature and fresh beginnings.",
            "Often evoking images of forests and verdant fields.",
            "A hue that suggests growth without giving too much away."
        ],
        "helpful": [
            "It is associated with life, renewal, and natural beauty.",
            "Commonly seen in foliage and natural landscapes.",
            "Its soothing presence is a staple in organic designs."
        ]
    },
    "yellow": {
        "vague": [
            "A bright shade that hints at warmth and light.",
            "Often reminiscent of soft, glowing sunshine.",
            "A gentle burst of color that lifts the mood."
        ],
        "helpful": [
            "It is a primary color that radiates warmth and optimism.",
            "Often used to evoke feelings of cheerfulness and energy.",
            "Its luminous quality makes it a favorite in many designs."
        ]
    },
    "purple": {
        "vague": [
            "A deep, mysterious hue that flirts with luxury.",
            "Often linked to creativity and subtle magic.",
            "A color that carries an air of enigma and grace."
        ],
        "helpful": [
            "It is historically associated with royalty and mysticism.",
            "Often used to suggest creativity and a touch of the exotic.",
            "Its uncommon nature sets it apart in a vivid palette."
        ]
    },
    "orange": {
        "vague": [
            "A vibrant tone that radiates energy and fun.",
            "Often evoking images of sunsets and autumn leaves.",
            "A lively color that hints at warmth without being overt."
        ],
        "helpful": [
            "It is a blend of red and yellow, exuding bold energy.",
            "Commonly used to inspire enthusiasm and creativity.",
            "Its brightness makes it a memorable accent in design."
        ]
    },
    "pink": {
        "vague": [
            "A soft, playful color that flirts with charm.",
            "Often linked to tender moments and lighthearted fun.",
            "A gentle shade that is both subtle and inviting."
        ],
        "helpful": [
            "It is a delicate hue often used to evoke warmth and affection.",
            "Commonly seen in nature’s softer expressions and creative art.",
            "Its understated tone adds a touch of whimsy to any design."
        ]
    },
    "brown": {
        "vague": [
            "A warm, earthy tone that feels natural and grounded.",
            "Often associated with rustic charm and reliability.",
            "A color that evokes the essence of wood and earth."
        ],
        "helpful": [
            "It is common in nature, symbolizing stability and comfort.",
            "Often used to represent organic materials and tradition.",
            "Its natural vibe makes it a subtle background for other colors."
        ]
    },
    "black": {
        "vague": [
            "A classic, mysterious hue that absorbs all light.",
            "Often linked to elegance and understated power.",
            "A color that speaks volumes without saying a word."
        ],
        "helpful": [
            "It is a timeless color often associated with sophistication.",
            "Used to evoke depth, formality, and modern style.",
            "Its stark simplicity makes it both versatile and striking."
        ]
    },
    "white": {
        "vague": [
            "A clean, pure color that opens up any space.",
            "Often seen as a blank canvas full of possibility.",
            "A neutral tone that quietly complements any palette."
        ],
        "helpful": [
            "It is associated with simplicity, clarity, and fresh starts.",
            "Often used as a background to make other colors pop.",
            "Its unassuming nature makes it a universal design choice."
        ]
    },

    # Sports
    "soccer": {
        "vague": [
            "A globally adored game played on lush, green fields.",
            "Often seen as a dance of strategy and spontaneous play.",
            "A sport that unites fans through simple, fast-paced action."
        ],
        "helpful": [
            "It involves two teams trying to score by kicking a ball.",
            "Known for its free-flowing play and passionate supporters.",
            "Its minimal equipment and universal appeal make it a worldwide favorite."
        ]
    },
    "basketball": {
        "vague": [
            "A dynamic game where the court becomes a stage.",
            "Often remembered for its fast breaks and soaring leaps.",
            "A sport that pulses with energy and split-second decisions."
        ],
        "helpful": [
            "It involves shooting a ball through a raised hoop.",
            "Known for its mix of individual flair and team coordination.",
            "Its fast-paced, high-scoring nature captivates audiences."
        ]
    },
    "tennis": {
        "vague": [
            "A game of finesse played on a neatly marked court.",
            "Often seen as a battle of endurance and precision.",
            "A sport where swift movements and sharp reflexes reign."
        ],
        "helpful": [
            "It involves hitting a small ball with a racket over a net.",
            "Known for its graceful footwork and competitive rallies.",
            "Its blend of power and strategy makes it an enduring favorite."
        ]
    },
    "baseball": {
        "vague": [
            "A time-honored game evoking nostalgic summer days.",
            "Often linked to leisurely afternoons and community cheers.",
            "A sport that unfolds on a diamond of dreams."
        ],
        "helpful": [
            "It involves hitting a pitched ball and running around bases.",
            "Known for its rich tradition and strategic play.",
            "Its slow pace mixed with moments of brilliance makes it unique."
        ]
    },
    "golf": {
        "vague": [
            "A quiet pursuit played on sprawling, manicured greens.",
            "Often viewed as a test of precision under calm skies.",
            "A sport where every swing is a measured act of focus."
        ],
        "helpful": [
            "It involves driving a ball into a series of holes with minimal strokes.",
            "Known for its serene courses and emphasis on accuracy.",
            "Its blend of patience and skill appeals to many."
        ]
    },
    "boxing": {
        "vague": [
            "A combat sport that pits agility against sheer will.",
            "Often associated with raw power and endurance.",
            "A contest where every punch tells a story."
        ],
        "helpful": [
            "It involves two opponents exchanging blows in a ring.",
            "Known for its strategic footwork and explosive action.",
            "Its intensity and focus make it a test of grit."
        ]
    },
    "cricket": {
        "vague": [
            "A bat-and-ball game with a leisurely yet strategic pace.",
            "Often linked with long, sunlit days and tactical play.",
            "A sport that unfolds slowly with moments of brilliance."
        ],
        "helpful": [
            "It involves batting, bowling, and fielding in a carefully timed match.",
            "Known for its intricate rules and deep-rooted traditions.",
            "Its blend of patience and strategy captivates its fans."
        ]
    },
    "swimming": {
        "vague": [
            "A sport where fluid motion meets cool refreshment.",
            "Often seen as a graceful race against time and water.",
            "A challenge that tests both speed and endurance in liquid form."
        ],
        "helpful": [
            "It involves racing across water in pools or open water.",
            "Known for its emphasis on streamlined form and stamina.",
            "Its clean, rhythmic strokes define the essence of the sport."
        ]
    },
    "cycling": {
        "vague": [
            "A journey on two wheels through winding paths.",
            "Often linked with adventure and scenic escapades.",
            "A sport that blends speed with the beauty of nature."
        ],
        "helpful": [
            "It involves pedaling through various terrains with determination.",
            "Known for its balance of power, endurance, and technique.",
            "Its competitive and recreational forms both capture hearts."
        ]
    },
    "volleyball": {
        "vague": [
            "A high-energy game played with a bouncing ball and soaring leaps.",
            "Often seen as a contest of quick reflexes and smooth teamwork.",
            "A sport where every set and spike creates a lively rhythm."
        ],
        "helpful": [
            "It involves keeping a ball in the air by passing it over a net.",
            "Known for its fast-paced rallies and coordinated plays.",
            "Its mix of athleticism and strategy makes it a crowd favorite."
        ]
    },

    # Jobs
    "teacher": {
        "vague": [
            "A guide in a world of endless questions.",
            "Often seen as a mentor in a bustling classroom.",
            "A role that sparks curiosity without giving all the answers."
        ],
        "helpful": [
            "It involves sharing knowledge and inspiring new ideas.",
            "Known for nurturing minds and igniting creativity.",
            "Its impact is measured by the spark it lights in learners."
        ]
    },
    "doctor": {
        "vague": [
            "A healer who works behind the scenes of wellness.",
            "Often pictured in a realm of care and constant motion.",
            "A figure who mends bodies with a touch of mystery."
        ],
        "helpful": [
            "It involves diagnosing ailments and providing remedies.",
            "Known for a blend of science, compassion, and steady hands.",
            "Its practice is crucial for restoring health and hope."
        ]
    },
    "engineer": {
        "vague": [
            "A creator who turns abstract ideas into tangible designs.",
            "Often associated with innovation and clever fixes.",
            "A mind that constructs solutions out of thin air."
        ],
        "helpful": [
            "It involves designing systems and solving technical puzzles.",
            "Known for analytical skills and a practical approach.",
            "Its work builds the foundation of modern conveniences."
        ]
    },
    "chef": {
        "vague": [
            "A culinary wizard blending flavors into art.",
            "Often seen as a master of secret recipes.",
            "A creative force behind every delicious dish."
        ],
        "helpful": [
            "It involves preparing meals that delight both taste and sight.",
            "Known for combining ingredients into memorable flavors.",
            "Its expertise transforms everyday food into experiences."
        ]
    },
    "artist": {
        "vague": [
            "A dreamer who paints the world in unique colors.",
            "Often lost in creative reverie and vibrant visions.",
            "A soul whose work speaks in subtle, unexpected ways."
        ],
        "helpful": [
            "It involves expressing ideas through visual or auditory media.",
            "Known for a perspective that sees beauty in the mundane.",
            "Its creations evoke emotions without spelling everything out."
        ]
    },
    "pilot": {
        "vague": [
            "A navigator of skies filled with endless blue.",
            "Often pictured as a free spirit riding on clouds.",
            "A person who turns the horizon into a playground."
        ],
        "helpful": [
            "It involves steering aircraft and ensuring safe journeys.",
            "Known for precise skills and calm decision-making under pressure.",
            "Its role keeps travelers aloft and on schedule."
        ]
    },
    "nurse": {
        "vague": [
            "A caring presence in the midst of life’s urgencies.",
            "Often seen as a comforting figure in bustling wards.",
            "A guardian of health whose touch eases pain."
        ],
        "helpful": [
            "It involves providing essential care and emotional support.",
            "Known for its empathy and critical role in patient recovery.",
            "Its work is a blend of medical skill and compassionate care."
        ]
    },
    "firefighter": {
        "vague": [
            "A brave soul who rushes toward danger in silence.",
            "Often seen as a beacon of hope amidst chaos.",
            "A guardian who faces fire with steadfast resolve."
        ],
        "helpful": [
            "It involves battling blazes and rescuing those in peril.",
            "Known for quick reflexes and unyielding courage.",
            "Its duty is to protect life and property under extreme conditions."
        ]
    },
    "police": {
        "vague": [
            "A vigilant presence that maintains order in the streets.",
            "Often seen as a silent guardian of community peace.",
            "A figure whose role is wrapped in duty and resolve."
        ],
        "helpful": [
            "It involves enforcing laws and ensuring public safety.",
            "Known for its constant vigilance and commitment to justice.",
            "Its presence helps keep neighborhoods safe and orderly."
        ]
    },
    "musician": {
        "vague": [
            "A creator who breathes life into sound and rhythm.",
            "Often seen as a storyteller without uttering words.",
            "A soul who transforms silence into moving melodies."
        ],
        "helpful": [
            "It involves composing or performing music that stirs the heart.",
            "Known for a passion that resonates in every note.",
            "Its craft turns everyday sounds into an art form."
        ]
    },

    # Vehicles
    "car": {
        "vague": [
            "A common mode of modern transportation.",
            "Often seen cruising down highways.",
            "A compact machine built for speed and comfort."
        ],
        "helpful": [
            "It typically has four wheels and an engine.",
            "Used for daily commuting and road trips.",
            "Its design balances performance with practicality."
        ]
    },
    "bicycle": {
        "vague": [
            "A two-wheeled vehicle powered by human effort.",
            "Often a symbol of eco-friendly travel.",
            "A simple machine that blends fitness and freedom."
        ],
        "helpful": [
            "It has pedals and a chain mechanism.",
            "Used for commuting and leisurely rides.",
            "Its design is lightweight and efficient."
        ]
    },
    "airplane": {
        "vague": [
            "A soaring machine that defies gravity.",
            "Often associated with long journeys and high altitudes.",
            "A vehicle that carries people across continents."
        ],
        "helpful": [
            "It has wings, engines, and a fuselage.",
            "Used for fast, long-distance travel.",
            "Its design focuses on aerodynamics and speed."
        ]
    },
    "train": {
        "vague": [
            "A long, connected series of vehicles on tracks.",
            "Often seen as a symbol of industrial progress.",
            "A mode of transport that weaves through landscapes."
        ],
        "helpful": [
            "It is powered by diesel, electricity, or steam.",
            "Used for both commuter and long-distance travel.",
            "Its cars connect to form a single, efficient system."
        ]
    },
    "boat": {
        "vague": [
            "A vessel that moves gracefully on water.",
            "Often associated with leisure and adventure.",
            "A means of travel on lakes, rivers, or seas."
        ],
        "helpful": [
            "It is designed to float and navigate waterways.",
            "Used for fishing, cruising, or competitive sailing.",
            "Its design prioritizes buoyancy and balance."
        ]
    },
    "motorcycle": {
        "vague": [
            "A two-wheeled motor vehicle known for its agility.",
            "Often linked to freedom on open roads.",
            "A compact machine that exudes cool energy."
        ],
        "helpful": [
            "It has an engine and is built for speed.",
            "Used for fast travel and spirited rides.",
            "Its design emphasizes maneuverability and style."
        ]
    },
    "bus": {
        "vague": [
            "A large vehicle designed to transport many people.",
            "Often a workhorse of urban transit.",
            "A common sight in public transportation."
        ],
        "helpful": [
            "It features multiple doors and ample seating.",
            "Used to shuttle crowds across cities.",
            "Its design focuses on capacity and efficiency."
        ]
    },
    "helicopter": {
        "vague": [
            "A rotorcraft that hovers and takes off vertically.",
            "Often associated with emergency services.",
            "A vehicle that can access remote or congested areas."
        ],
        "helpful": [
            "It uses rotors for lift and propulsion.",
            "Commonly deployed for rescues and aerial views.",
            "Its compact design makes it versatile in flight."
        ]
    },
    "submarine": {
        "vague": [
            "A vessel that delves beneath the waves.",
            "Often shrouded in deep-sea mystery.",
            "A machine that navigates the underwater realm."
        ],
        "helpful": [
            "It is built to operate under high water pressure.",
            "Used in military, research, and exploration.",
            "Its design allows it to submerge and resurface safely."
        ]
    },
    "truck": {
        "vague": [
            "A heavy-duty vehicle designed for hauling.",
            "Often seen transporting goods on highways.",
            "A robust machine built for carrying loads."
        ],
        "helpful": [
            "It has a large cargo area and a powerful engine.",
            "Essential in logistics and freight transport.",
            "Its design emphasizes strength and durability."
        ]
    },

    # Mythology
    "zeus": {
        "vague": [
            "A powerful god ruling the skies.",
            "Often depicted wielding lightning.",
            "A figure of supreme authority in ancient lore."
        ],
        "helpful": [
            "King of the Greek gods, ruling over the heavens.",
            "Known for his thunderbolt and majestic presence.",
            "His domain includes the sky and weather."
        ]
    },
    "odin": {
        "vague": [
            "A wise, one-eyed deity shrouded in mystery.",
            "Often associated with sacrifice and wisdom.",
            "A powerful figure from Norse legends."
        ],
        "helpful": [
            "Chief of the Norse gods, seeking knowledge at all costs.",
            "Recognized for his one eye and his runic secrets.",
            "His symbols include ravens and a spear."
        ]
    },
    "anubis": {
        "vague": [
            "A guardian of the underworld in ancient tales.",
            "Often linked with mummification and death.",
            "A figure guiding souls to the afterlife."
        ],
        "helpful": [
            "Egyptian god associated with embalming and funerary rites.",
            "Recognized by his jackal head and protective role.",
            "He ensures safe passage for souls into the afterlife."
        ]
    },
    "poseidon": {
        "vague": [
            "A mighty god ruling the seas.",
            "Often depicted with a trident.",
            "A force of nature both calm and tempestuous."
        ],
        "helpful": [
            "Greek god of the sea, earthquakes, and horses.",
            "His trident controls the waves and storms.",
            "He is known for both his wrath and his benevolence."
        ]
    },
    "hades": {
        "vague": [
            "A mysterious ruler of the realm of the dead.",
            "Often depicted in dark, somber tones.",
            "A figure whose domain is the underworld."
        ],
        "helpful": [
            "Greek god of the underworld, overseeing the dead.",
            "Known for his solemn, grim authority.",
            "His presence reminds mortals of life's impermanence."
        ]
    },
    "thor": {
        "vague": [
            "A thunderous god wielding a mighty hammer.",
            "Often portrayed as a fierce protector.",
            "A warrior deity with a stormy presence."
        ],
        "helpful": [
            "Norse god of thunder, famous for his hammer Mjölnir.",
            "Celebrated for his strength and heroic deeds.",
            "His battles are the stuff of legend."
        ]
    },
    "ares": {
        "vague": [
            "A fierce deity embodying the chaos of battle.",
            "Often depicted amid the clamor of war.",
            "A symbol of raw, unbridled aggression."
        ],
        "helpful": [
            "Greek god of war, representing conflict and strife.",
            "Known for his temper and martial prowess.",
            "His influence is felt on battlefields."
        ]
    },
    "isis": {
        "vague": [
            "A nurturing goddess revered for her magic.",
            "Often associated with healing and protection.",
            "A figure of ancient wisdom and fertility."
        ],
        "helpful": [
            "Egyptian goddess known for her restorative powers.",
            "Celebrated for her role as a mother and healer.",
            "Her mythology centers on protection and rebirth."
        ]
    },
    "kraken": {
        "vague": [
            "A legendary sea monster of immense size.",
            "Often whispered about in sailor's tales.",
            "A creature of myth lurking in the deep."
        ],
        "helpful": [
            "A fabled beast said to have massive tentacles.",
            "Known for causing terror in ancient maritime lore.",
            "Its myth represents the mystery of the ocean depths."
        ]
    },
    "phoenix": {
        "vague": [
            "A mythical bird reborn from its ashes.",
            "Often associated with fire and renewal.",
            "A symbol of eternal rebirth and hope."
        ],
        "helpful": [
            "A legendary creature that cyclically regenerates.",
            "Its flames consume the old to bring forth the new.",
            "It stands as a metaphor for transformation and immortality."
        ]
    },

    # Technology
    "computer": {
        "vague": [
            "A modern marvel that processes vast data.",
            "Often seen as the heart of digital innovation.",
            "A device that transforms information into power."
        ],
        "helpful": [
            "It executes programs and performs complex calculations.",
            "An essential tool in modern work and play.",
            "Its evolution has revolutionized global communication."
        ]
    },
    "smartphone": {
        "vague": [
            "A compact device connecting you to the world.",
            "Often a symbol of modern communication.",
            "A gadget that fits in your pocket yet spans the globe."
        ],
        "helpful": [
            "It combines telephony with powerful computing.",
            "A personal assistant, camera, and communicator in one.",
            "Its interface has transformed how we interact with technology."
        ]
    },
    "robot": {
        "vague": [
            "A mechanical being programmed to serve.",
            "Often depicted in futuristic visions.",
            "A creation that blurs the line between man and machine."
        ],
        "helpful": [
            "It automates tasks and can perform repetitive actions.",
            "Used in industries from manufacturing to exploration.",
            "Its development continues to shape the future of work."
        ]
    },
    "drone": {
        "vague": [
            "A flying machine that operates without a pilot.",
            "Often seen capturing aerial views.",
            "A device that hovers above with silent precision."
        ],
        "helpful": [
            "It is used for photography, surveillance, and delivery.",
            "Operated remotely or autonomously for various tasks.",
            "Its compact design enables agile flight in tight spaces."
        ]
    },
    "satellite": {
        "vague": [
            "A silent guardian orbiting the Earth.",
            "Often linked with global communications.",
            "A machine that watches over from space."
        ],
        "helpful": [
            "It relays signals for weather, navigation, and data.",
            "An essential component of modern telecommunications.",
            "Its orbit ensures continuous coverage of the planet."
        ]
    },
    "internet": {
        "vague": [
            "An invisible web that connects the world.",
            "Often described as a digital ecosystem.",
            "A realm where information flows without borders."
        ],
        "helpful": [
            "It enables global connectivity and communication.",
            "Used for social interaction, business, and entertainment.",
            "Its infrastructure is the backbone of the modern world."
        ]
    },
    "server": {
        "vague": [
            "A robust machine that stores and serves data.",
            "Often hidden in massive data centers.",
            "A workhorse of the digital age."
        ],
        "helpful": [
            "It processes requests and delivers information.",
            "Crucial for hosting websites, apps, and services.",
            "Its performance is key to online experiences."
        ]
    },
    "algorithm": {
        "vague": [
            "A set of instructions that solves problems step by step.",
            "Often hidden behind the magic of computation.",
            "A blueprint for decision-making in code."
        ],
        "helpful": [
            "It provides a systematic method to solve tasks.",
            "Used in everything from search engines to recommendation systems.",
            "Its efficiency can be a game-changer in software performance."
        ]
    },
    "database": {
        "vague": [
            "A structured repository of organized information.",
            "Often considered the backbone of data-driven systems.",
            "A digital vault where data is carefully stored."
        ],
        "helpful": [
            "It efficiently stores and retrieves large volumes of data.",
            "Critical for applications ranging from banking to social media.",
            "Its structure is key to managing and accessing information."
        ]
    },
    "chip": {
        "vague": [
            "A tiny component that powers modern electronics.",
            "Often called the brain of digital devices.",
            "A micro marvel that enables complex computing."
        ],
        "helpful": [
            "It performs millions of calculations per second.",
            "Essential for smartphones, computers, and appliances.",
            "Its miniaturization is a cornerstone of modern technology."
        ]
    },

    # Languages
    "english": {
        "vague": [
            "A global language of literature and commerce.",
            "Often a bridge between diverse cultures.",
            "A language known for its flexibility and reach."
        ],
        "helpful": [
            "It is widely used as a common language worldwide.",
            "Its vocabulary is vast and continually evolving.",
            "Its influence is seen in media, business, and education."
        ]
    },
    "spanish": {
        "vague": [
            "A language with a rhythmic and passionate sound.",
            "Often linked to vibrant cultures and lively conversation.",
            "A tongue that dances with emotion and flair."
        ],
        "helpful": [
            "It is spoken by millions across the globe.",
            "Known for its expressive intonation and regional diversity.",
            "Its literature and music are rich with history and passion."
        ]
    },
    "french": {
        "vague": [
            "A language synonymous with romance and art.",
            "Often admired for its elegance and charm.",
            "A tongue that flows like poetry."
        ],
        "helpful": [
            "It is considered a language of culture and diplomacy.",
            "Famous for its contributions to art, cuisine, and fashion.",
            "Its refined pronunciation and style are celebrated."
        ]
    },
    "mandarin": {
        "vague": [
            "A tonal language steeped in ancient tradition.",
            "Often seen as the language of a vast empire.",
            "A language where each character tells a story."
        ],
        "helpful": [
            "It is the most spoken language in the world.",
            "Known for its logographic writing system.",
            "Its tonal nature and characters make it uniquely challenging."
        ]
    },
    "arabic": {
        "vague": [
            "A language rich in poetry and historical depth.",
            "Often resonating with a rhythmic cadence.",
            "A tongue that carries centuries of legacy."
        ],
        "helpful": [
            "It is widely spoken in the Middle East and North Africa.",
            "Famous for its beautiful calligraphy and expressive vocabulary.",
            "Its grammar and script have influenced many cultures."
        ]
    },
    "hindi": {
        "vague": [
            "A vibrant language spoken by millions.",
            "Often filled with expressive intonation and warmth.",
            "A language that intertwines tradition with modernity."
        ],
        "helpful": [
            "It is one of the official languages of India.",
            "Known for its poetic expression and rich heritage.",
            "Its script and sounds reflect a diverse cultural tapestry."
        ]
    },
    "russian": {
        "vague": [
            "A language of deep literature and powerful emotion.",
            "Often described as robust and resonant.",
            "A tongue that carries the weight of history."
        ],
        "helpful": [
            "It is the most widely spoken Slavic language.",
            "Noted for its complex grammar and expressive vocabulary.",
            "Its literary tradition is renowned across the globe."
        ]
    },
    "portuguese": {
        "vague": [
            "A melodic language with a soulful cadence.",
            "Often linked to seafaring adventures and warm cultures.",
            "A language spoken across continents with charm."
        ],
        "helpful": [
            "It is the official language of Portugal and Brazil.",
            "Known for its lyrical intonation and expressive style.",
            "Its influence is felt in music, art, and literature."
        ]
    },
    "japanese": {
        "vague": [
            "A language where tradition meets modernity.",
            "Often noted for its politeness and precision.",
            "A tongue with a unique blend of elegance and formality."
        ],
        "helpful": [
            "It employs kanji along with two syllabaries.",
            "Known for its succinct expressions and rich culture.",
            "Its writing system and grammar offer a distinct charm."
        ]
    },
    "german": {
        "vague": [
            "A language known for its precision and structure.",
            "Often characterized by its compound words and clarity.",
            "A tongue that exudes strength and order."
        ],
        "helpful": [
            "It is widely used in science, engineering, and philosophy.",
            "Noted for its systematic grammar and extensive vocabulary.",
            "Its literary and cultural contributions are globally significant."
        ]
    },

    # Food (New)
    "pizza": {
        "vague": [
            "A savory pie with endless topping possibilities.",
            "Often associated with casual, fun gatherings.",
            "A dish that blends cheese, sauce, and dough."
        ],
        "helpful": [
            "It typically features a crispy crust with melted cheese and tomato sauce.",
            "Known for its versatility with countless toppings.",
            "A favorite comfort food in many cultures."
        ]
    },
    "burger": {
        "vague": [
            "A hearty sandwich stacked with savory goodness.",
            "Often linked to fast-food and casual dining.",
            "A meaty delight between two buns."
        ],
        "helpful": [
            "It usually includes a beef patty, cheese, and various condiments.",
            "Popular worldwide as a filling, customizable meal.",
            "Its combination of flavors and textures is widely enjoyed."
        ]
    },
    "sushi": {
        "vague": [
            "A delicate dish wrapped in seaweed.",
            "Often associated with Japanese culinary art.",
            "A bite-sized treat with a touch of elegance."
        ],
        "helpful": [
            "It typically consists of vinegared rice paired with fish or vegetables.",
            "Known for its artful presentation and fresh ingredients.",
            "Its flavors range from subtle to bold depending on the type."
        ]
    },
    "taco": {
        "vague": [
            "A handheld delight with a crunchy shell.",
            "Often associated with festive street food.",
            "A compact meal bursting with flavor."
        ],
        "helpful": [
            "It usually features seasoned meat, salsa, and vegetables wrapped in a tortilla.",
            "Loved for its combination of spicy, tangy, and savory tastes.",
            "A versatile dish that can be customized in many ways."
        ]
    },
    "pasta": {
        "vague": [
            "A staple of Italian cuisine with endless shapes.",
            "Often seen as a comfort food for many.",
            "A dish that pairs well with a variety of sauces."
        ],
        "helpful": [
            "It comes in many forms like spaghetti, penne, or fettuccine.",
            "Often served with tomato-based, cream, or pesto sauces.",
            "Its simplicity and heartiness make it a favorite meal."
        ]
    },
    "salad": {
        "vague": [
            "A fresh mix of vegetables and sometimes fruits.",
            "Often regarded as a healthy, light meal.",
            "A dish that can be both crunchy and refreshing."
        ],
        "helpful": [
            "It usually includes greens, vegetables, and a dressing.",
            "Popular as a starter or side dish for its lightness.",
            "Its ingredients can be varied to suit many tastes."
        ]
    },
    "steak": {
        "vague": [
            "A robust cut of meat, often grilled to perfection.",
            "Often linked to hearty, satisfying meals.",
            "A dish that embodies simplicity and indulgence."
        ],
        "helpful": [
            "It is typically a beef cut, best enjoyed medium-rare.",
            "Known for its rich flavor and tender texture when cooked right.",
            "A classic favorite for meat lovers."
        ]
    },
    "chocolate": {
        "vague": [
            "A sweet treat with a rich, indulgent flavor.",
            "Often associated with desserts and celebrations.",
            "A beloved confection enjoyed worldwide."
        ],
        "helpful": [
            "It can be dark, milk, or white, each with a unique taste.",
            "Known for its smooth texture and ability to melt in your mouth.",
            "A versatile ingredient in both sweet and savory dishes."
        ]
    },
    "ice cream": {
        "vague": [
            "A frozen dessert that cools and delights.",
            "Often a treat on hot summer days.",
            "A scoop of creamy, sweet indulgence."
        ],
        "helpful": [
            "It comes in many flavors and is served cold.",
            "Known for its smooth, creamy texture and refreshing taste.",
            "A popular dessert that can be topped with various goodies."
        ]
    },
    "sandwich": {
        "vague": [
            "A portable meal stacked between slices of bread.",
            "Often seen as a quick, satisfying bite.",
            "A versatile dish that can be both simple and gourmet."
        ],
        "helpful": [
            "It usually contains layers of meat, cheese, and vegetables.",
            "Loved for its convenience and endless variations.",
            "A common choice for lunches and picnics."
        ]
    },

    # Movies (New)
    "inception": {
        "vague": [
            "A mind-bending tale of dreams within dreams.",
            "Often described as a cerebral journey.",
            "A film that blurs the line between reality and illusion."
        ],
        "helpful": [
            "It features complex layers of the subconscious.",
            "Known for its innovative narrative and striking visuals.",
            "A modern classic that challenges perception."
        ]
    },
    "titanic": {
        "vague": [
            "A tragic romance set against an ill-fated voyage.",
            "Often remembered for its epic scale and emotion.",
            "A film that blends love with disaster."
        ],
        "helpful": [
            "It tells the story of a doomed ship and a timeless romance.",
            "Known for its groundbreaking visuals and emotional impact.",
            "A cinematic epic that left a lasting legacy."
        ]
    },
    "avatar": {
        "vague": [
            "A visually stunning journey to a distant world.",
            "Often described as an immersive alien experience.",
            "A film that transports viewers to another reality."
        ],
        "helpful": [
            "It features groundbreaking visual effects and 3D imagery.",
            "Known for its lush, alien landscapes and rich culture.",
            "A movie that redefined modern filmmaking techniques."
        ]
    },
    "gladiator": {
        "vague": [
            "An epic tale of honor and betrayal in ancient times.",
            "Often remembered for its fierce battles and heroic spirit.",
            "A film that captures the essence of ancient valor."
        ],
        "helpful": [
            "It follows the journey of a fallen general seeking vengeance.",
            "Known for its powerful performances and historical grandeur.",
            "A stirring saga of power, loyalty, and redemption."
        ]
    },
    "matrix": {
        "vague": [
            "A futuristic film questioning the nature of reality.",
            "Often described as a blend of philosophy and action.",
            "A movie that challenges the fabric of existence."
        ],
        "helpful": [
            "It features groundbreaking special effects and complex ideas.",
            "Known for its iconic action sequences and cyberpunk aesthetics.",
            "A film that left a significant mark on pop culture."
        ]
    },
    "jaws": {
        "vague": [
            "A suspenseful tale of terror beneath the waves.",
            "Often associated with a lurking menace in the deep.",
            "A film that made the ocean seem dangerously vast."
        ],
        "helpful": [
            "It tells the story of a great white shark terrorizing a beach town.",
            "Known for its suspenseful score and groundbreaking terror.",
            "A classic thriller that changed the face of horror movies."
        ]
    },
    "star wars": {
        "vague": [
            "A legendary saga of heroes in a distant galaxy.",
            "Often remembered for its epic space battles.",
            "A film series that redefined science fiction."
        ],
        "helpful": [
            "It features a battle between good and evil across the stars.",
            "Known for its iconic characters and groundbreaking special effects.",
            "A cultural phenomenon that spawned a vast universe of lore."
        ]
    },
    "godfather": {
        "vague": [
            "A tale of power, family, and betrayal.",
            "Often seen as a deep dive into a criminal underworld.",
            "A film that explores loyalty and legacy."
        ],
        "helpful": [
            "It follows the life of a mafia family and its intricate dynamics.",
            "Known for its profound storytelling and memorable quotes.",
            "A timeless classic that set the standard for gangster films."
        ]
    },
    "rocky": {
        "vague": [
            "An underdog story that inspires and uplifts.",
            "Often remembered for its gritty determination.",
            "A film that embodies perseverance against all odds."
        ],
        "helpful": [
            "It tells the story of a boxer rising from obscurity to fame.",
            "Known for its motivational training montages and heartfelt story.",
            "A cinematic triumph of grit, heart, and determination."
        ]
    },
    "casablanca": {
        "vague": [
            "A timeless romance set against war-torn backdrops.",
            "Often remembered for its bittersweet farewell.",
            "A film that blends love with sacrifice."
        ],
        "helpful": [
            "It tells a story of lost love and sacrifice during conflict.",
            "Known for its iconic lines and enduring emotional impact.",
            "A classic that remains one of cinema's greatest romances."
        ]
    },

    # Video Games (New)
    "mario": {
        "vague": [
            "A plucky plumber embarking on daring adventures.",
            "Often recognized by his red cap and mustache.",
            "A character whose jumps have inspired generations."
        ],
        "helpful": [
            "He rescues princesses and faces countless foes in a pixelated world.",
            "Famous for his iconic power-ups and cheerful optimism.",
            "A beloved figure in video game history."
        ]
    },
    "zelda": {
        "vague": [
            "A legendary quest filled with puzzles and magic.",
            "Often linked to a heroic journey in a mystical land.",
            "A series that blends adventure with ancient lore."
        ],
        "helpful": [
            "It follows a hero who battles evil to save a kingdom.",
            "Known for its intricate dungeons and timeless soundtrack.",
            "A hallmark of adventure and fantasy in gaming."
        ]
    },
    "minecraft": {
        "vague": [
            "A blocky world where creativity is limitless.",
            "Often associated with endless building and exploration.",
            "A game that turns imagination into a virtual reality."
        ],
        "helpful": [
            "Players mine resources and build structures from pixelated blocks.",
            "Known for its survival mode and creative sandbox.",
            "A phenomenon that sparked a generation of builders."
        ]
    },
    "doom": {
        "vague": [
            "A fast-paced shooter set in a demon-infested realm.",
            "Often remembered for its intense, adrenaline-fueled action.",
            "A game that redefined the shooter genre."
        ],
        "helpful": [
            "It features aggressive combat against otherworldly foes.",
            "Known for its heavy metal soundtrack and immersive action.",
            "A groundbreaking title that set new standards in gaming."
        ]
    },
    "fortnite": {
        "vague": [
            "A battle royale where survival is the ultimate goal.",
            "Often noted for its colorful, ever-changing arenas.",
            "A game that blends construction with intense combat."
        ],
        "helpful": [
            "Players build, fight, and strategize in a fast-paced world.",
            "Known for its frequent updates and pop culture references.",
            "A modern sensation that revolutionized multiplayer gaming."
        ]
    },
    "tetris": {
        "vague": [
            "A simple yet captivating puzzle of falling shapes.",
            "Often hailed as a timeless classic.",
            "A game that challenges spatial awareness and quick thinking."
        ],
        "helpful": [
            "It involves arranging tetrominoes to complete horizontal lines.",
            "Known for its hypnotic gameplay and rhythmic falling blocks.",
            "A minimalist puzzle that has stood the test of time."
        ]
    },
    "halo": {
        "vague": [
            "A futuristic shooter set in a vast, interstellar war.",
            "Often associated with epic battles and advanced armor.",
            "A game that combines science fiction with intense action."
        ],
        "helpful": [
            "It follows a super-soldier fighting against alien forces.",
            "Known for its rich lore and multiplayer experiences.",
            "A landmark title in the first-person shooter genre."
        ]
    },
    "pac-man": {
        "vague": [
            "A yellow circle on a quest to gobble dots.",
            "Often considered a pioneer in arcade gaming.",
            "A character whose maze adventures are legendary."
        ],
        "helpful": [
            "It involves navigating mazes while avoiding colorful ghosts.",
            "Known for its simple yet addictive gameplay.",
            "A timeless icon of the arcade era."
        ]
    },
    "sonic": {
        "vague": [
            "A fast, blue hedgehog with a need for speed.",
            "Often synonymous with high-octane adventures.",
            "A game character who races through loops and obstacles."
        ],
        "helpful": [
            "He uses his super speed to overcome challenges and foes.",
            "Known for his iconic attitude and vibrant world.",
            "A beloved mascot of the classic video game era."
        ]
    },
    "counter-strike": {
        "vague": [
            "A tactical shooter where teamwork is key.",
            "Often recognized for its competitive multiplayer battles.",
            "A game that demands precision and strategy."
        ],
        "helpful": [
            "It pits teams against each other in high-stakes combat scenarios.",
            "Known for its realistic gameplay and strategic depth.",
            "A cornerstone of competitive esports."
        ]
    },

    # Literature (New)
    "hamlet": {
        "vague": [
            "A tragic tale of revenge and introspection.",
            "Often hailed as one of the greatest plays.",
            "A story where doubt and destiny intertwine."
        ],
        "helpful": [
            "It follows the troubled prince seeking vengeance.",
            "Known for its profound soliloquies and dramatic tension.",
            "A timeless work exploring themes of mortality and betrayal."
        ]
    },
    "1984": {
        "vague": [
            "A dystopian vision of a controlled society.",
            "Often cited as a warning against totalitarianism.",
            "A novel that challenges freedom and truth."
        ],
        "helpful": [
            "It portrays a future where surveillance and propaganda reign.",
            "Known for its bleak outlook and powerful social commentary.",
            "A classic that remains relevant in discussions of privacy."
        ]
    },
    "dune": {
        "vague": [
            "An epic saga set on a desert planet.",
            "Often described as a blend of politics and prophecy.",
            "A story of survival and power in a harsh world."
        ],
        "helpful": [
            "It explores complex themes of ecology, religion, and politics.",
            "Known for its rich world-building and intricate plot.",
            "A landmark in science fiction literature."
        ]
    },
    "gatsby": {
        "vague": [
            "A tale of glamour and hidden despair.",
            "Often set against the backdrop of lavish parties.",
            "A story where dreams and reality collide."
        ],
        "helpful": [
            "It follows a mysterious millionaire and his unfulfilled longing.",
            "Known for its lyrical prose and timeless exploration of the American Dream.",
            "A novel that critiques social stratification and excess."
        ]
    },
    "moby dick": {
        "vague": [
            "A relentless pursuit on the high seas.",
            "Often seen as a journey into obsession.",
            "A story of man versus nature."
        ],
        "helpful": [
            "It chronicles the hunt for a legendary white whale.",
            "Known for its deep symbolism and complex narrative.",
            "A classic work exploring the depths of human ambition."
        ]
    },
    "frankenstein": {
        "vague": [
            "A chilling tale of creation and consequence.",
            "Often considered a pioneer of science fiction horror.",
            "A story where ambition and ethics collide."
        ],
        "helpful": [
            "It follows a scientist whose experiment brings unintended terror.",
            "Known for its exploration of humanity and the nature of life.",
            "A novel that questions the boundaries of scientific exploration."
        ]
    },
    "pride": {
        "vague": [
            "A classic narrative of love and societal expectations.",
            "Often paired with another famous work.",
            "A story that critiques class and romance."
        ],
        "helpful": [
            "It is part of a famous duo exploring love and prejudice.",
            "Known for its witty dialogue and social commentary.",
            "A timeless novel examining manners and morality."
        ]
    },
    "prejudice": {
        "vague": [
            "A counterpart to a story of love and judgment.",
            "Often cited alongside themes of romance and class.",
            "A narrative questioning societal norms."
        ],
        "helpful": [
            "It delves into issues of bias and societal expectations.",
            "Known for its sharp critique of social hierarchy.",
            "A work that remains influential in discussions of equality."
        ]
    },
    "crime": {
        "vague": [
            "A dark exploration of moral dilemmas and justice.",
            "Often delving into the human psyche.",
            "A narrative that questions right and wrong."
        ],
        "helpful": [
            "It investigates the consequences of transgressions and guilt.",
            "Known for its psychological depth and moral inquiry.",
            "A novel that challenges the notion of absolute justice."
        ]
    },
    "punishment": {
        "vague": [
            "A story of remorse, redemption, and the human condition.",
            "Often regarded as a deep dive into personal suffering.",
            "A narrative where every action has its consequence."
        ],
        "helpful": [
            "It follows a troubled soul confronting the weight of his actions.",
            "Known for its intense introspection and philosophical insights.",
            "A classic work examining guilt, atonement, and morality."
        ]
    },
        # TV Shows
    "friends": {
        "vague": [
            "A sitcom about a close-knit group in a bustling city.",
            "Often linked to coffee shop hangouts and witty banter.",
            "A show about the ups and downs of friendship."
        ],
        "helpful": [
            "It features six main characters navigating life in New York.",
            "Known for its iconic Central Perk and memorable catchphrases.",
            "A beloved series that defined a generation's humor."
        ]
    },
    "breaking bad": {
        "vague": [
            "A dark drama of transformation and consequence.",
            "Often seen as a descent into a dangerous world.",
            "A story where a teacher becomes a criminal mastermind."
        ],
        "helpful": [
            "It follows a high school chemistry teacher turned meth manufacturer.",
            "Known for its intense character development and moral dilemmas.",
            "A critically acclaimed series about power and downfall."
        ]
    },
    "the office": {
        "vague": [
            "A quirky look at everyday office life.",
            "Often filled with awkward moments and dry humor.",
            "A mockumentary capturing the absurdities of work."
        ],
        "helpful": [
            "It portrays the daily lives of office workers in a mundane setting.",
            "Famous for its offbeat humor and memorable characters.",
            "A series that redefined workplace comedy."
        ]
    },
    "game of thrones": {
        "vague": [
            "A sprawling fantasy of power and betrayal.",
            "Often filled with dragons, intrigue, and epic battles.",
            "A tale of kingdoms at war."
        ],
        "helpful": [
            "It follows multiple noble families vying for a throne.",
            "Known for its complex plot twists and dramatic conflicts.",
            "A high-fantasy series celebrated for its grand scale."
        ]
    },
    "stranger things": {
        "vague": [
            "A nostalgic mystery set in a small town.",
            "Often laced with supernatural secrets and retro vibes.",
            "A tale of kids facing eerie, unknown forces."
        ],
        "helpful": [
            "It involves a missing boy and otherworldly occurrences.",
            "Known for its blend of 80s nostalgia and suspenseful storytelling.",
            "A show that mixes friendship, mystery, and supernatural elements."
        ]
    },

    # Historical Figures
    "einstein": {
        "vague": [
            "A genius with a wild mane of hair.",
            "Often depicted as the face of brilliance.",
            "A man whose ideas reshaped science."
        ],
        "helpful": [
            "Famous for his theory of relativity and playful demeanor.",
            "His contributions to physics revolutionized our understanding of space and time.",
            "A symbol of intellectual curiosity and creative thought."
        ]
    },
    "cleopatra": {
        "vague": [
            "A regal figure from ancient times.",
            "Often surrounded by mystery and allure.",
            "A queen known for her captivating charm."
        ],
        "helpful": [
            "Renowned for her political acumen and beauty.",
            "She ruled ancient Egypt with both grace and power.",
            "Her life story is one of romance, ambition, and intrigue."
        ]
    },
    "lincoln": {
        "vague": [
            "A tall figure from a pivotal era.",
            "A man of humble beginnings with great resolve.",
            "An icon of unity and freedom."
        ],
        "helpful": [
            "Known for abolishing slavery and guiding a nation through war.",
            "His leadership and honesty are deeply revered.",
            "A president whose legacy is built on emancipation and unity."
        ]
    },
    "gandhi": {
        "vague": [
            "A peaceful visionary with profound influence.",
            "Often seen as the embodiment of nonviolence.",
            "A humble leader with unwavering resolve."
        ],
        "helpful": [
            "Renowned for his philosophy of nonviolence and civil rights.",
            "He inspired movements for freedom across the globe.",
            "His legacy is centered on peaceful resistance and justice."
        ]
    },
    "napoleon": {
        "vague": [
            "A short man with towering ambition.",
            "Often seen as a brilliant yet controversial leader.",
            "A figure whose military campaigns reshaped nations."
        ],
        "helpful": [
            "Famous for his strategic genius and the Napoleonic Code.",
            "His rise and fall left an indelible mark on Europe.",
            "A leader remembered for both his conquests and his complex legacy."
        ]
    },
        "spongebob": {
        "vague": [
            "A bubbly character living under the sea.",
            "Often cheerful and full of quirky adventures.",
            "A sponge with an infectious optimism."
        ],
        "helpful": [
            "He lives in a pineapple and works at the Krusty Krab.",
            "Known for his upbeat personality and memorable antics.",
            "His world is filled with friends and silly escapades."
        ]
    },
    "tom and jerry": {
        "vague": [
            "A classic duo locked in a timeless chase.",
            "Often a battle of wits between predator and prey.",
            "A pair whose rivalry is legendary."
        ],
        "helpful": [
            "They engage in clever, slapstick pursuits with endless creativity.",
            "Known for their silent, expressive humor and playful antics.",
            "Their endless chases have entertained audiences for generations."
        ]
    },
    "looney tunes": {
        "vague": [
            "A collection of zany characters and wild antics.",
            "Often filled with anarchic humor and surreal gags.",
            "A series where the absurd is celebrated."
        ],
        "helpful": [
            "It features icons like Bugs Bunny and Daffy Duck.",
            "Known for its clever wordplay and offbeat scenarios.",
            "Its legacy has influenced animated comedy for decades."
        ]
    },
    "rick and morty": {
        "vague": [
            "A wild, interdimensional adventure with dark humor.",
            "Often blending sci-fi elements with absurdity.",
            "A duo exploring bizarre alternate realities."
        ],
        "helpful": [
            "It follows a genius scientist and his quirky grandson on surreal journeys.",
            "Known for its irreverent humor and clever narrative twists.",
            "Its mix of existential themes and comedy has redefined adult animation."
        ]
    },
    "simpsons": {
        "vague": [
            "A long-running saga of a quirky family in a small town.",
            "Often a satirical reflection of everyday life.",
            "A series full of colorful characters and memorable lines."
        ],
        "helpful": [
            "It portrays the adventures of the Simpson family in Springfield.",
            "Known for its humor, catchphrases, and cultural impact.",
            "Its legacy spans decades as a commentary on modern society."
        ]
    },
    "futurama": {
        "vague": [
            "A futuristic romp mixing space travel with absurd comedy.",
            "Often featuring quirky characters in a sci-fi setting.",
            "A show that blends humor with cosmic adventures."
        ],
        "helpful": [
            "It follows a delivery boy frozen in time and revived in the future.",
            "Known for its clever satire and imaginative scenarios.",
            "Its creative world-building makes it a cult favorite."
        ]
    },
    "adventure time": {
        "vague": [
            "A whimsical world of magic and quirky heroes.",
            "Often filled with surreal adventures and colorful landscapes.",
            "A series where fantasy and humor collide."
        ],
        "helpful": [
            "It follows a boy and his magical dog on epic quests.",
            "Known for its imaginative storytelling and heartfelt moments.",
            "Its blend of adventure and absurdity has captured a wide audience."
        ]
    },
    "regular show": {
        "vague": [
            "A slice-of-life cartoon with unexpected twists.",
            "Often turning mundane tasks into surreal escapades.",
            "A show where ordinary becomes extraordinary."
        ],
        "helpful": [
            "It revolves around two friends navigating bizarre, everyday challenges.",
            "Known for its offbeat humor and quirky characters.",
            "Its blend of the mundane with the absurd makes it uniquely entertaining."
        ]
    },
    "powerpuff girls": {
        "vague": [
            "Three super-powered siblings saving the day with charm.",
            "Often depicted as cute yet incredibly fierce.",
            "A cartoon where innocence meets heroism."
        ],
        "helpful": [
            "They use their unique powers to defeat villains in style.",
            "Known for their vibrant colors and dynamic teamwork.",
            "Their adventures blend fun, action, and a touch of sweetness."
        ]
    },
    "peppa pig": {
        "vague": [
            "A lovable piglet with simple, playful adventures.",
            "Often associated with early childhood fun.",
            "A character who brings gentle humor and warmth."
        ],
        "helpful": [
            "She stars in lighthearted stories that are easy to follow.",
            "Known for her friendly demeanor and relatable antics.",
            "Her world is filled with simple lessons and cheerful moments."
        ]
    },
        "batman": {
        "vague": [
            "A dark vigilante in a city of shadows.",
            "Often seen brooding on rooftops.",
            "A hero with a mysterious past."
        ],
        "helpful": [
            "He fights crime in Gotham with his intellect and gadgets.",
            "Known for his detective skills and iconic cape.",
            "His mission is to bring justice without superpowers."
        ]
    },
    "superman": {
        "vague": [
            "A man of steel with extraordinary abilities.",
            "Often seen soaring through the sky.",
            "A beacon of hope and power."
        ],
        "helpful": [
            "He hails from another planet and protects Earth.",
            "Known for his super strength, flight, and x-ray vision.",
            "His symbol is a shining emblem of hope."
        ]
    },
    "spiderman": {
        "vague": [
            "A nimble hero with a knack for climbing.",
            "Often associated with webs and quick reflexes.",
            "A friendly neighborhood protector."
        ],
        "helpful": [
            "He uses his spider-like powers to swing through the city.",
            "Known for his witty comebacks and agile moves.",
            "His origin involves a fateful, radioactive encounter."
        ]
    },
    "wolverine": {
        "vague": [
            "A fierce mutant with an unbreakable spirit.",
            "Often depicted with retractable claws.",
            "A rugged fighter with a troubled past."
        ],
        "helpful": [
            "He possesses rapid healing and razor-sharp claws.",
            "Known for his gruff demeanor and survival instinct.",
            "His resilience and determination define his legacy."
        ]
    },
    "iron man": {
        "vague": [
            "A genius billionaire encased in a high-tech suit.",
            "Often seen as a symbol of innovation.",
            "A hero who fuses technology with charisma."
        ],
        "helpful": [
            "He relies on an advanced suit powered by an arc reactor.",
            "Known for his witty remarks and inventive gadgets.",
            "His leadership and ingenuity inspire his allies."
        ]
    },
    "deadpool": {
        "vague": [
            "A wisecracking antihero with a penchant for chaos.",
            "Often breaking the fourth wall with humor.",
            "A mercenary whose irreverence knows no bounds."
        ],
        "helpful": [
            "He mixes regenerative powers with sharp, unpredictable humor.",
            "Known for his offbeat style and over-the-top antics.",
            "His irreverence and skill make him a cult favorite."
        ]
    },
    "hulk": {
        "vague": [
            "A massive, green powerhouse fueled by anger.",
            "Often seen as a force of raw strength.",
            "A creature defined by uncontrollable fury."
        ],
        "helpful": [
            "He transforms into a towering figure when provoked.",
            "Known for his unstoppable force and iconic roar.",
            "His internal struggle between intellect and rage is legendary."
        ]
    },
    "wonder woman": {
        "vague": [
            "A warrior princess with unmatched determination.",
            "Often depicted with a golden lasso and regal poise.",
            "A symbol of strength and compassion."
        ],
        "helpful": [
            "She combines combat skills with an unwavering sense of justice.",
            "Known for her divine heritage and fearless leadership.",
            "Her mission is to promote peace and equality."
        ]
    },
    "flash": {
        "vague": [
            "A hero whose speed defies the limits of time.",
            "Often a blur of red and gold in motion.",
            "A figure who races through danger in a flash."
        ],
        "helpful": [
            "He moves so quickly he seems to bend time itself.",
            "Known for his rapid reflexes and quick wit.",
            "His ability to outrun almost anything is his defining trait."
        ]
    },
    "aquaman": {
        "vague": [
            "A ruler of the deep with a commanding presence.",
            "Often linked with the mysteries of the ocean.",
            "A hero who bridges two realms."
        ],
        "helpful": [
            "He leads an underwater kingdom with wisdom and might.",
            "Known for his ability to communicate with sea life.",
            "His adventures span both the ocean depths and the surface world."
        ]
    },
        "eiffel tower": {
        "vague": [
            "An iconic iron structure reaching toward the sky.",
            "Often seen as a symbol of romance and innovation.",
            "A landmark admired worldwide for its elegance."
        ],
        "helpful": [
            "It stands in Paris, showcasing intricate lattice work.",
            "Famous for its panoramic views and historic charm.",
            "Its silhouette is instantly recognizable as a beacon of art."
        ]
    },
    "great wall": {
        "vague": [
            "A sprawling barrier winding across rugged terrain.",
            "Often viewed as an ancient marvel of defense.",
            "A monumental structure that spans vast distances."
        ],
        "helpful": [
            "It was built to safeguard an empire from invaders.",
            "Known for its impressive length and rugged construction.",
            "Its history reflects centuries of human effort and resilience."
        ]
    },
    "pyramids": {
        "vague": [
            "Mysterious structures steeped in ancient lore.",
            "Often linked to the secrets of a bygone civilization.",
            "A wonder of the ancient world shrouded in enigma."
        ],
        "helpful": [
            "They were built as tombs for Egypt's pharaohs.",
            "Known for their precise alignment and enduring mystique.",
            "Their grandeur and history continue to captivate visitors."
        ]
    },
    "statue of liberty": {
        "vague": [
            "A towering symbol of freedom and welcome.",
            "Often depicted as a gift representing hope.",
            "A majestic figure holding aloft a radiant torch."
        ],
        "helpful": [
            "It stands proudly at the entrance of New York Harbor.",
            "Known for its powerful symbolism of liberty and democracy.",
            "Its green patina and design inspire awe and unity."
        ]
    },
    "colosseum": {
        "vague": [
            "An ancient arena echoing with the roar of crowds.",
            "Often seen as a relic of epic gladiatorial contests.",
            "A monumental structure that speaks of bygone battles."
        ],
        "helpful": [
            "It remains a testament to Roman engineering and culture.",
            "Famous for its architectural grandeur and historical depth.",
            "Its ruins tell tales of glory and the harsh realities of combat."
        ]
    },
    "taj mahal": {
        "vague": [
            "A breathtaking monument of love and art.",
            "Often described as a marble masterpiece.",
            "A symbol of eternal romance and exquisite beauty."
        ],
        "helpful": [
            "It was built as a tribute to undying love in India.",
            "Known for its intricate carvings and reflective pools.",
            "Its symmetry and elegance make it one of the world’s most admired structures."
        ]
    },
    "big ben": {
        "vague": [
            "A historic clock tower that marks the passage of time.",
            "Often more famous for its chimes than its appearance.",
            "A symbol of precision and timeless tradition."
        ],
        "helpful": [
            "It stands as an iconic landmark in London.",
            "Known for its resonant bell and classic design.",
            "Its chimes have echoed across the city for generations."
        ]
    },
    "sydney opera house": {
        "vague": [
            "A striking architectural marvel by the water.",
            "Often celebrated for its sail-like design.",
            "A cultural landmark with an instantly recognizable silhouette."
        ],
        "helpful": [
            "It serves as a premier venue for the performing arts in Australia.",
            "Known for its innovative design and artistic impact.",
            "Its unique roof shells make it a modern icon of architecture."
        ]
    },
    "christ the redeemer": {
        "vague": [
            "A monumental statue overlooking a vibrant city.",
            "Often depicted with outstretched arms in a welcoming pose.",
            "A symbol of faith and hope seen from above."
        ],
        "helpful": [
            "It towers over Rio de Janeiro as a beacon of peace.",
            "Known for its art deco style and spiritual symbolism.",
            "Its grand scale and outstretched arms inspire unity."
        ]
    },
    "machu picchu": {
        "vague": [
            "An ancient citadel perched high in the mountains.",
            "Often shrouded in mist and mystery.",
            "A lost city that speaks of a storied past."
        ],
        "helpful": [
            "It is an Incan ruin nestled in the Andes of Peru.",
            "Known for its breathtaking terraces and enigmatic history.",
            "Its remote location and stunning architecture captivate visitors."
        ]
    },
        "rock": {
        "vague": [
            "A genre known for its raw, electrifying energy.",
            "Often driven by powerful guitar riffs.",
            "A style that shakes the ground with its sound."
        ],
        "helpful": [
            "It features strong beats and electrifying solos.",
            "Famous for energetic live performances and anthemic choruses.",
            "Its rebellious spirit has defined generations of music."
        ]
    },
    "pop": {
        "vague": [
            "A catchy genre that appeals to the masses.",
            "Often upbeat and instantly memorable.",
            "A style that lingers in your mind all day."
        ],
        "helpful": [
            "It emphasizes memorable hooks and danceable beats.",
            "Known for its widespread radio play and chart-topping hits.",
            "Its simplicity and appeal have made it a global phenomenon."
        ]
    },
    "jazz": {
        "vague": [
            "A smooth genre full of improvisation and soul.",
            "Often characterized by intricate rhythms and cool vibes.",
            "A style that flows like a spontaneous conversation."
        ],
        "helpful": [
            "It features complex chords and spontaneous solos.",
            "Known for its expressive improvisation and rich history.",
            "Its fusion of structure and freedom creates a uniquely soulful sound."
        ]
    },
    "classical": {
        "vague": [
            "A timeless genre of orchestral masterpieces.",
            "Often associated with grand symphonies and elegant compositions.",
            "A style that has withstood the test of time."
        ],
        "helpful": [
            "It encompasses compositions from multiple eras and forms.",
            "Known for its structured harmonies and emotive themes.",
            "Its works are celebrated in concert halls worldwide."
        ]
    },
    "hip-hop": {
        "vague": [
            "A rhythmic genre that blends beats with storytelling.",
            "Often characterized by sharp lyrics and dynamic flow.",
            "A style that reflects urban culture and creativity."
        ],
        "helpful": [
            "It features strong, punchy beats and spoken word elements.",
            "Known for its cultural impact and expressive lyricism.",
            "Its influence spans decades and continually evolves with its community."
        ]
    },
    "electronic": {
        "vague": [
            "A futuristic genre built on synthesized sounds.",
            "Often associated with digital beats and dance floors.",
            "A style that pulses with innovation and energy."
        ],
        "helpful": [
            "It relies on electronic instruments and computer-based production.",
            "Known for its ability to create immersive, pulsating soundscapes.",
            "Its diverse subgenres include techno, house, and trance."
        ]
    },
    "country": {
        "vague": [
            "A genre that tells stories of life on the open road.",
            "Often infused with heartfelt lyrics and acoustic charm.",
            "A style that reflects rural traditions and simplicity."
        ],
        "helpful": [
            "It emphasizes storytelling, simple melodies, and twangy vocals.",
            "Famous for its narrative songs and relatable themes.",
            "Its honest, straightforward style resonates with many."
        ]
    },
    "blues": {
        "vague": [
            "A soulful genre that speaks of hardship and hope.",
            "Often characterized by expressive guitar riffs and emotional vocals.",
            "A style that channels deep, heartfelt emotions."
        ],
        "helpful": [
            "It typically follows a 12-bar structure and expressive solos.",
            "Known for its raw emotion and influence on other music styles.",
            "Its melancholic yet healing sound has touched many lives."
        ]
    },
    "reggae": {
        "vague": [
            "A laid-back genre with a rhythmic, offbeat groove.",
            "Often associated with island vibes and social messages.",
            "A style that radiates chill, positive energy."
        ],
        "helpful": [
            "It features syncopated rhythms, prominent bass, and uplifting lyrics.",
            "Known for its role in promoting peace and unity.",
            "Its distinctive sound has made it a symbol of Caribbean culture."
        ]
    },
    "metal": {
        "vague": [
            "An intense genre with powerful, aggressive sound.",
            "Often characterized by heavy guitar riffs and dynamic drumming.",
            "A style that pushes musical limits with raw energy."
        ],
        "helpful": [
            "It is marked by distorted guitars, pounding drums, and vigorous vocals.",
            "Known for its passionate fan base and diverse subgenres.",
            "Its bold, cathartic sound is both challenging and exhilarating."
        ]
    },

}

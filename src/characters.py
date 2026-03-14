"""
Character Library & Band Roles
-------------------------------
20 anthropomorphic animal characters + 8 band roles.
Each character has detailed visual descriptions for consistent video generation.
"""

# ── 8 Band Roles ──────────────────────────────────────────────
BAND_ROLES = {
    "vocalist": {
        "name": "Lead Vocalist",
        "description": "The frontperson of the band, singing into a microphone at center stage",
        "instrument": "microphone",
        "stage_position": "center stage, front",
    },
    "guitarist": {
        "name": "Lead Guitarist",
        "description": "Playing electric guitar with energetic riffs and solos",
        "instrument": "electric guitar",
        "stage_position": "stage right, front",
    },
    "bassist": {
        "name": "Bass Guitarist",
        "description": "Grooving on a bass guitar, keeping the rhythm tight",
        "instrument": "bass guitar",
        "stage_position": "stage left, front",
    },
    "drummer": {
        "name": "Drummer",
        "description": "Behind the drum kit, driving the beat with sticks flying",
        "instrument": "drum kit",
        "stage_position": "center stage, back",
    },
    "keyboardist": {
        "name": "Keyboardist",
        "description": "Playing a keyboard/synthesizer, adding melodic layers",
        "instrument": "keyboard synthesizer",
        "stage_position": "stage left, back",
    },
    "saxophonist": {
        "name": "Saxophonist",
        "description": "Playing a golden saxophone with smooth, soulful melodies",
        "instrument": "saxophone",
        "stage_position": "stage right, back",
    },
    "violinist": {
        "name": "Violinist",
        "description": "Playing a violin with expressive, sweeping bow movements",
        "instrument": "violin",
        "stage_position": "stage right, middle",
    },
    "dj": {
        "name": "DJ / Turntablist",
        "description": "Behind a DJ booth with turntables and mixer, scratching and mixing",
        "instrument": "DJ turntables and mixer",
        "stage_position": "stage left, elevated platform",
    },
}

# ── 20 Animal Characters ─────────────────────────────────────
# Each character has a highly detailed visual description for consistent
# video generation across multiple clips.
ANIMAL_CHARACTERS = {
    "rocky_bear": {
        "name": "Rocky the Bear",
        "species": "Brown Bear",
        "visual": (
            "A large, muscular anthropomorphic brown bear with warm chocolate-brown fur, "
            "a cream-colored muzzle and belly patch. He has small round ears, deep amber eyes, "
            "and a friendly wide grin. He wears a black leather vest with silver studs over a "
            "red flannel shirt, ripped blue jeans, and black biker boots. His paws are oversized "
            "and expressive. He has a small silver earring in his left ear."
        ),
        "personality": "The confident powerhouse — big, loud, and full of heart",
    },
    "luna_cat": {
        "name": "Luna the Cat",
        "species": "Siamese Cat",
        "visual": (
            "A sleek, elegant anthropomorphic Siamese cat with creamy ivory fur and dark brown "
            "points on her ears, face mask, paws, and tail. She has striking bright blue almond-shaped "
            "eyes with long lashes, a delicate pink nose, and long whiskers. She wears a shimmering "
            "purple sequin crop top, high-waisted black leather pants, and silver ankle boots. "
            "She has a thin silver chain necklace with a crescent moon pendant."
        ),
        "personality": "Cool, mysterious diva with effortless grace",
    },
    "max_dog": {
        "name": "Max the Dog",
        "species": "Golden Retriever",
        "visual": (
            "A cheerful, energetic anthropomorphic golden retriever with fluffy golden-blonde fur, "
            "floppy ears, a big wet black nose, and a constantly wagging tail. He has warm brown "
            "puppy-dog eyes and a wide happy smile with his tongue slightly out. He wears a bright "
            "orange Hawaiian shirt with tropical flower prints, khaki cargo shorts, and green "
            "high-top sneakers. He has a red bandana tied around his neck."
        ),
        "personality": "The eternally happy, enthusiastic good boy of the group",
    },
    "jazz_rabbit": {
        "name": "Jazz the Rabbit",
        "species": "Dutch Rabbit",
        "visual": (
            "A tall, slim anthropomorphic rabbit with soft white fur and distinctive black patches "
            "over both eyes and ears. She has long upright ears with pink insides, large expressive "
            "violet eyes, a tiny pink twitching nose, and long graceful whiskers. She wears a "
            "vintage emerald green velvet blazer over a white turtleneck, slim black trousers, "
            "and polished brown oxford shoes. She has round gold-rimmed glasses perched on her nose."
        ),
        "personality": "The intellectual artist — sophisticated, witty, and rhythmically gifted",
    },
    "spike_hedgehog": {
        "name": "Spike the Hedgehog",
        "species": "Hedgehog",
        "visual": (
            "A small, spunky anthropomorphic hedgehog with brown spines tipped in electric blue, "
            "a soft tan belly and face, tiny round ears, and bright green eyes full of mischief. "
            "He has a small pointy snout with a black button nose. He wears a torn black band "
            "t-shirt with a lightning bolt logo, skinny red plaid pants, and chunky black combat "
            "boots with neon green laces. He has a chain wallet and multiple ear piercings."
        ),
        "personality": "The punk rebel — small but fierce, full of electric energy",
    },
    "coco_panda": {
        "name": "Coco the Panda",
        "species": "Giant Panda",
        "visual": (
            "A round, cuddly anthropomorphic giant panda with classic black and white fur — "
            "white face with black eye patches, black ears, and a plump white belly. She has "
            "large sparkling dark brown eyes with a gentle, dreamy expression. She wears a "
            "pastel pink hoodie with a small strawberry embroidered on the chest, light blue "
            "denim overalls, and white platform sneakers with pink laces. She has a small "
            "flower hairpin behind her left ear."
        ),
        "personality": "The sweet, lovable one who melts everyone's hearts",
    },
    "blaze_fox": {
        "name": "Blaze the Fox",
        "species": "Red Fox",
        "visual": (
            "A sharp, cunning anthropomorphic red fox with vibrant orange-red fur, a white chest "
            "and chin, and a large bushy tail with a white tip. He has piercing golden-yellow eyes, "
            "pointed ears with black tips, and a narrow snout with a confident smirk. He wears a "
            "sleek dark navy blue suit jacket over a black V-neck t-shirt, fitted dark gray jeans, "
            "and polished black Chelsea boots. He has aviator sunglasses pushed up on his head."
        ),
        "personality": "The suave showman — charming, quick, and always stylish",
    },
    "ella_elephant": {
        "name": "Ella the Elephant",
        "species": "African Elephant",
        "visual": (
            "A tall, graceful anthropomorphic elephant with soft gray skin, large fan-shaped ears "
            "with pink inner edges, a long expressive trunk, and small kind hazel eyes with thick "
            "lashes. She wears an elegant flowing golden-yellow maxi dress with a bold African-print "
            "sash around her waist, chunky wooden bead bracelets on both wrists, and strappy "
            "brown leather sandals. She has a small tiara of wildflowers on her head."
        ),
        "personality": "The gentle giant — soulful, wise, and deeply musical",
    },
    "ricky_raccoon": {
        "name": "Ricky the Raccoon",
        "species": "Raccoon",
        "visual": (
            "A scrappy, nimble anthropomorphic raccoon with gray-brown fur, his signature black "
            "mask marking around mischievous bright green eyes, and a bushy ringed tail with "
            "alternating black and gray stripes. He has small rounded ears and dexterous hand-like "
            "paws. He wears a backwards red snapback cap, a baggy white graphic tee with a turntable "
            "print, oversized cargo pants, and classic black-and-white checkered slip-on shoes. "
            "He has headphones hanging around his neck."
        ),
        "personality": "The street-smart trickster — crafty, playful, and surprisingly talented",
    },
    "melody_owl": {
        "name": "Melody the Owl",
        "species": "Barn Owl",
        "visual": (
            "A stately anthropomorphic barn owl with a heart-shaped white facial disc, golden-brown "
            "feathered back and wings speckled with silver spots, and large round dark eyes that "
            "seem to see everything. She has a small curved beak and feathery ear tufts. She wears "
            "a deep burgundy velvet cape over a cream lace blouse, a long flowing dark skirt, "
            "and Victorian-style lace-up boots. She carries a conductor's baton tucked in her belt."
        ),
        "personality": "The nocturnal maestro — wise, mysterious, and musically brilliant",
    },
    "bubbles_frog": {
        "name": "Bubbles the Frog",
        "species": "Tree Frog",
        "visual": (
            "A small, bouncy anthropomorphic tree frog with bright lime-green skin, a pale yellow "
            "belly, and large bulging orange eyes with horizontal black pupils. He has wide webbed "
            "feet and sticky finger pads. He wears a funky tie-dye rainbow t-shirt, baggy purple "
            "harem pants, and open-toed sandals. He has a peace-sign necklace and a flower crown "
            "of daisies on his head. His skin glistens with a slight moisture sheen."
        ),
        "personality": "The groovy free spirit — chill, funky, and always vibing",
    },
    "thunder_wolf": {
        "name": "Thunder the Wolf",
        "species": "Gray Wolf",
        "visual": (
            "A tall, powerful anthropomorphic gray wolf with thick silver-gray fur, a white chest, "
            "and a darker gray mane running down the back of his neck. He has intense ice-blue eyes, "
            "a strong angular snout, pointed ears, and sharp canine teeth visible in his confident grin. "
            "He wears a long black trench coat over a white dress shirt with rolled-up sleeves, "
            "dark fitted pants, and heavy black military boots. He has a silver wolf-fang pendant."
        ),
        "personality": "The intense lone wolf — powerful vocals, brooding yet magnetic",
    },
    "poppy_penguin": {
        "name": "Poppy the Penguin",
        "species": "Emperor Penguin",
        "visual": (
            "A short, adorable anthropomorphic emperor penguin with classic black and white tuxedo "
            "plumage, a golden-yellow patch on each side of her neck, and a bright orange beak. "
            "She has round shiny black eyes full of enthusiasm and small flipper-wings that she "
            "waves expressively. She wears a sparkling silver sequin bow tie, a miniature top hat "
            "tilted to the side, white gloves, and tiny black tap shoes. She waddles with charm."
        ),
        "personality": "The showstopper — tiny, theatrical, and born to perform",
    },
    "samba_parrot": {
        "name": "Samba the Parrot",
        "species": "Scarlet Macaw",
        "visual": (
            "A vibrant, flamboyant anthropomorphic scarlet macaw with brilliant red feathers on the "
            "body, bright blue and yellow wing feathers, a long red and blue tail, and a strong "
            "curved black beak. He has round white eye patches with small dark eyes and a feathered "
            "crest that he raises when excited. He wears a flashy gold lamé open-front shirt showing "
            "his red chest feathers, white bell-bottom pants, and gold platform boots. He has "
            "multiple gold rings and a feathered boa scarf."
        ),
        "personality": "The flamboyant showbird — loud, colorful, and irresistibly entertaining",
    },
    "indie_deer": {
        "name": "Indie the Deer",
        "species": "White-tailed Deer",
        "visual": (
            "A gentle, graceful anthropomorphic deer with soft tawny-brown fur, a white belly and "
            "inner ears, and a small white tail. She has large doe eyes in deep warm brown, a "
            "small black nose, and elegant branching antlers wrapped with tiny fairy lights. She "
            "wears an oversized cozy mustard-yellow knit sweater, a plaid flannel skirt, brown "
            "leather ankle boots, and a woven friendship bracelet. She has a canvas tote bag "
            "covered in band patches slung over her shoulder."
        ),
        "personality": "The indie dreamer — gentle, artistic, and hauntingly beautiful vocals",
    },
    "duke_crocodile": {
        "name": "Duke the Crocodile",
        "species": "Crocodile",
        "visual": (
            "A big, imposing anthropomorphic crocodile with dark olive-green scaly skin, a lighter "
            "yellow-green underbelly, and a long powerful tail. He has a wide snout full of sharp "
            "teeth displayed in a permanent cool grin, and small intense yellow eyes with slit "
            "pupils. He wears a sharp pin-striped charcoal suit with a crisp white shirt open at "
            "the collar, a gold pocket watch chain, and shiny black wingtip shoes. He has a "
            "thick gold signet ring on his right hand."
        ),
        "personality": "The smooth operator — cool as ice, deep grooves, blues soul",
    },
    "pixel_chameleon": {
        "name": "Pixel the Chameleon",
        "species": "Panther Chameleon",
        "visual": (
            "A quirky, eye-catching anthropomorphic chameleon whose skin shifts between electric "
            "blue, hot pink, and neon green in swirling patterns. He has large turret-like eyes "
            "that move independently, a curled prehensile tail, and zygodactyl feet (two toes "
            "forward, two back). He wears a futuristic silver jacket with LED trim that glows, "
            "holographic pants that shimmer with rainbow colors, and transparent platform sneakers "
            "with lights inside. He has tiny headphones embedded in his head crest."
        ),
        "personality": "The tech-savvy wildcard — unpredictable, innovative, and visually mesmerizing",
    },
    "rosie_flamingo": {
        "name": "Rosie the Flamingo",
        "species": "Flamingo",
        "visual": (
            "A tall, elegant anthropomorphic flamingo with vibrant coral-pink plumage, long slender "
            "legs, and a gracefully curved neck. She has a distinctive downward-curved black-tipped "
            "pink beak, bright yellow eyes with glamorous false lashes, and delicate wing-arms with "
            "deeper magenta flight feathers. She wears a slinky black cocktail dress with a high "
            "slit, a long pearl necklace, elbow-length black satin gloves, and strappy gold "
            "stiletto heels. A single red rose is tucked behind her ear."
        ),
        "personality": "The glamorous diva — elegant, dramatic, and a voice like velvet",
    },
    "banjo_monkey": {
        "name": "Banjo the Monkey",
        "species": "Capuchin Monkey",
        "visual": (
            "A small, hyperactive anthropomorphic capuchin monkey with brown fur on the body, a "
            "lighter cream face and chest, and a long curling prehensile tail. He has large round "
            "curious brown eyes, big expressive ears, and a wide cheeky grin. He wears a bright "
            "yellow newsboy cap, a red-and-white striped vest over a white t-shirt, patched-up "
            "brown corduroy shorts, and no shoes (his feet are as nimble as his hands). He has "
            "a harmonica on a holder around his neck."
        ),
        "personality": "The hyperactive multi-instrumentalist — chaotic, playful, pure joy",
    },
    "aurora_snake": {
        "name": "Aurora the Snake",
        "species": "King Cobra",
        "visual": (
            "A sinuous, hypnotic anthropomorphic king cobra with iridescent scales that shift "
            "between deep purple, midnight blue, and emerald green. She has a dramatic expandable "
            "hood with golden eye-spot patterns, slitted golden eyes with an enigmatic gaze, and "
            "a forked tongue that flicks occasionally. She wears a fitted dark purple bodysuit with "
            "gold spiral patterns, long gold arm cuffs shaped like coiling snakes, and no shoes "
            "(her tail coils beneath). She has a gold circlet crown with an amethyst gem on her hood."
        ),
        "personality": "The mesmerizing enchantress — hypnotic, ethereal, otherworldly presence",
    },
}

# ── Preset band configurations ────────────────────────────────
BAND_PRESETS = {
    3: ["vocalist", "guitarist", "drummer"],
    4: ["vocalist", "guitarist", "bassist", "drummer"],
    5: ["vocalist", "guitarist", "bassist", "drummer", "keyboardist"],
    6: ["vocalist", "guitarist", "bassist", "drummer", "keyboardist", "saxophonist"],
    7: ["vocalist", "guitarist", "bassist", "drummer", "keyboardist", "saxophonist", "violinist"],
    8: ["vocalist", "guitarist", "bassist", "drummer", "keyboardist", "saxophonist", "violinist", "dj"],
}

# ── Default animal assignments per role ───────────────────────
DEFAULT_ASSIGNMENTS = {
    "vocalist": "thunder_wolf",
    "guitarist": "blaze_fox",
    "bassist": "duke_crocodile",
    "drummer": "rocky_bear",
    "keyboardist": "coco_panda",
    "saxophonist": "jazz_rabbit",
    "violinist": "indie_deer",
    "dj": "ricky_raccoon",
}


def get_band_roles(size: int) -> list[str]:
    """Get the list of band roles for a given band size (3-8)."""
    size = max(3, min(8, size))
    return BAND_PRESETS[size]


def build_band(size: int, assignments: dict[str, str] = None) -> list[dict]:
    """Build a band with animal characters assigned to roles.

    Args:
        size: Number of band members (3-8)
        assignments: Optional dict mapping role_id -> character_id.
                     Falls back to DEFAULT_ASSIGNMENTS for unspecified roles.

    Returns:
        List of dicts with full role + character info for each band member.
    """
    assignments = assignments or {}
    roles = get_band_roles(size)
    band = []

    for role_id in roles:
        char_id = assignments.get(role_id, DEFAULT_ASSIGNMENTS.get(role_id))
        role = BAND_ROLES[role_id]
        character = ANIMAL_CHARACTERS[char_id]

        band.append({
            "role_id": role_id,
            "role": role,
            "character_id": char_id,
            "character": character,
        })

    return band


def build_character_prompt(member: dict) -> str:
    """Build a detailed prompt string for a single band member."""
    char = member["character"]
    role = member["role"]
    return (
        f"{char['visual']} "
        f"This character is the {role['name']}, {role['description']}, "
        f"positioned at {role['stage_position']}."
    )


def build_band_prompt(band: list[dict], scene: str = "") -> str:
    """Build a full video prompt describing the entire band on stage.

    Args:
        band: List of band members from build_band()
        scene: Additional scene description (camera angle, mood, etc.)

    Returns:
        Detailed prompt for video generation.
    """
    member_descriptions = []
    for m in band:
        char = m["character"]
        role = m["role"]
        member_descriptions.append(
            f"{char['name']} ({char['species']}): {char['visual']} — "
            f"playing {role['instrument']} at {role['stage_position']}"
        )

    members_text = "; ".join(member_descriptions)

    prompt = (
        f"A cartoon animated music video scene of an anthropomorphic animal band "
        f"performing on a vibrant colorful stage. The band members are: {members_text}. "
        f"The characters are fully anthropomorphic, standing upright, with expressive faces "
        f"and dynamic body movements matching the music. "
        f"High quality 3D cartoon animation style, vibrant colors, dramatic stage lighting."
    )

    if scene:
        prompt += f" {scene}"

    return prompt


def build_closeup_prompt(member: dict, scene: str = "") -> str:
    """Build a close-up video prompt for a single band member.

    Args:
        member: A single band member dict from build_band()
        scene: Additional scene/mood description

    Returns:
        Detailed close-up prompt for video generation.
    """
    char = member["character"]
    role = member["role"]

    prompt = (
        f"Close-up shot in a cartoon animated music video. "
        f"{char['visual']} "
        f"This character is passionately {role['description']}. "
        f"The camera focuses on {char['name']} at {role['stage_position']}, "
        f"showing expressive face and dynamic movements. "
        f"High quality 3D cartoon animation, vibrant stage lighting, bokeh background."
    )

    if scene:
        prompt += f" {scene}"

    return prompt


def list_characters() -> str:
    """Return a formatted string listing all available characters."""
    lines = []
    for char_id, char in ANIMAL_CHARACTERS.items():
        lines.append(f"  {char_id:20s} — {char['name']} ({char['species']}): {char['personality']}")
    return "\n".join(lines)


def list_roles() -> str:
    """Return a formatted string listing all available band roles."""
    lines = []
    for role_id, role in BAND_ROLES.items():
        lines.append(f"  {role_id:15s} — {role['name']} ({role['instrument']})")
    return "\n".join(lines)

"""
Character Library & Band Roles
-------------------------------
20 anthropomorphic animal characters × 2 genders = 40 character variants.
8 band roles with stage positions.

All characters are designed to be:
- Cute, cool, and fashionable
- Professional musicians with fun personalities
- Friendly and approachable — never scary or intimidating
- Visually distinct with detailed outfits and accessories
"""

# ── 8 Band Roles ──────────────────────────────────────────────
BAND_ROLES = {
    "vocalist": {
        "name": "Lead Vocalist",
        "description": "The frontperson of the band, singing into a retro-style microphone at center stage",
        "instrument": "retro-style microphone on a stand",
        "stage_position": "center stage, front",
    },
    "guitarist": {
        "name": "Lead Guitarist",
        "description": "Playing a stylish electric guitar with energetic riffs and cool poses",
        "instrument": "electric guitar",
        "stage_position": "stage right, front",
    },
    "bassist": {
        "name": "Bass Guitarist",
        "description": "Grooving on a bass guitar with a relaxed cool vibe",
        "instrument": "bass guitar",
        "stage_position": "stage left, front",
    },
    "drummer": {
        "name": "Drummer",
        "description": "Behind a sparkly drum kit, keeping the beat with joyful energy",
        "instrument": "sparkly drum kit with colorful cymbals",
        "stage_position": "center stage, back on a raised platform",
    },
    "keyboardist": {
        "name": "Keyboardist",
        "description": "Playing a stylish keyboard synthesizer with smooth melodic lines",
        "instrument": "keyboard synthesizer with colorful keys",
        "stage_position": "stage left, back",
    },
    "saxophonist": {
        "name": "Saxophonist",
        "description": "Playing a shiny golden saxophone with smooth soulful melodies and cool swaying",
        "instrument": "shiny golden saxophone",
        "stage_position": "stage right, back",
    },
    "violinist": {
        "name": "Violinist",
        "description": "Playing a polished violin with graceful expressive bow movements",
        "instrument": "polished violin with a glossy finish",
        "stage_position": "stage right, middle",
    },
    "dj": {
        "name": "DJ / Turntablist",
        "description": "Behind a glowing neon DJ booth with turntables, mixing with flair",
        "instrument": "glowing neon DJ turntables and mixer",
        "stage_position": "stage left, elevated platform",
    },
}

# ── 20 Animal Characters (Male + Female variants) ────────────
# Each character has:
# - Cute, cool, fashionable appearance
# - Professional musician styling
# - Friendly, fun, approachable look
# - Detailed description for image generation consistency
#
# Visual descriptions are optimized for image generation prompts.

ANIMAL_CHARACTERS = {
    "rocky_bear": {
        "name": "Rocky the Bear",
        "species": "Brown Bear",
        "personality": "The warm-hearted powerhouse — big hugs, bigger beats",
        "male": {
            "visual": (
                "A friendly, cuddly anthropomorphic brown bear with soft chocolate-brown fur, "
                "round cute ears, warm honey-colored eyes, and a big cheerful smile. "
                "He has a cream-colored muzzle and round belly. "
                "He wears a stylish denim jacket with colorful music-note patches over a bright "
                "yellow graphic tee, cool ripped jeans with paint splatter details, and fresh white "
                "high-top sneakers. He has a fun beaded bracelet and a small star-shaped earring. "
                "Cute 3D cartoon style, friendly expression, soft rounded features."
            ),
            "image_prompt": (
                "Full body portrait of a cute friendly anthropomorphic brown bear character, "
                "standing upright, soft chocolate-brown fur, round ears, warm honey eyes, big smile, "
                "cream muzzle, wearing stylish denim jacket with music patches, bright yellow tee, "
                "cool ripped jeans, white high-top sneakers, beaded bracelet, star earring. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cute and cool musician look."
            ),
        },
        "female": {
            "visual": (
                "A friendly, cuddly anthropomorphic brown bear with soft chocolate-brown fur, "
                "round cute ears with tiny pink bows, warm honey-colored eyes with long lashes, "
                "and a big cheerful smile. She has a cream-colored muzzle and a cute round figure. "
                "She wears a trendy cropped pink bomber jacket over a sparkly white crop top, "
                "high-waisted mom jeans with flower embroidery, and pastel pink platform sneakers. "
                "She has a stack of colorful friendship bracelets and a small flower hairpin. "
                "Cute 3D cartoon style, friendly expression, soft rounded features."
            ),
            "image_prompt": (
                "Full body portrait of a cute friendly anthropomorphic female brown bear character, "
                "standing upright, soft chocolate-brown fur, round ears with pink bows, honey eyes "
                "with lashes, big smile, cream muzzle, wearing pink bomber jacket, sparkly white "
                "crop top, high-waisted jeans with flower embroidery, pink platform sneakers, "
                "friendship bracelets, flower hairpin. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cute and cool musician look."
            ),
        },
    },
    "luna_cat": {
        "name": "Luna the Cat",
        "species": "Siamese Cat",
        "personality": "The effortlessly cool trendsetter — graceful and stylish",
        "male": {
            "visual": (
                "A sleek, stylish anthropomorphic Siamese cat with creamy ivory fur and soft brown "
                "points on ears, face, paws, and tail. He has bright sparkling blue eyes, "
                "a cute pink nose, neat whiskers, and a confident friendly smile. "
                "He wears a cool lavender silk bomber jacket over a black turtleneck, "
                "slim tailored charcoal pants, and sleek white leather boots. "
                "He has a silver chain necklace with a crescent moon pendant and trendy round sunglasses "
                "pushed up on his head. Cute 3D cartoon style, cool and fashionable."
            ),
            "image_prompt": (
                "Full body portrait of a cute stylish anthropomorphic male Siamese cat character, "
                "standing upright, ivory fur, brown points, bright blue eyes, pink nose, friendly smile, "
                "wearing lavender silk bomber jacket, black turtleneck, charcoal pants, white boots, "
                "silver moon necklace, round sunglasses on head. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cool fashionable musician look."
            ),
        },
        "female": {
            "visual": (
                "A sleek, elegant anthropomorphic Siamese cat with creamy ivory fur and soft brown "
                "points on ears, face, paws, and tail. She has bright sparkling blue almond-shaped "
                "eyes with cute long lashes, a delicate pink nose, neat whiskers, and a sweet smile. "
                "She wears a shimmering lavender sequin crop top, a stylish high-waisted black "
                "pleated skirt, and sparkly silver ankle boots. "
                "She has a dainty silver chain necklace with a crescent moon pendant and a small "
                "glittery hair clip. Cute 3D cartoon style, elegant and fashionable."
            ),
            "image_prompt": (
                "Full body portrait of a cute elegant anthropomorphic female Siamese cat character, "
                "standing upright, ivory fur, brown points, bright blue eyes with lashes, pink nose, "
                "sweet smile, wearing lavender sequin crop top, black pleated skirt, silver ankle boots, "
                "moon pendant necklace, glittery hair clip. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cute fashionable musician look."
            ),
        },
    },
    "max_dog": {
        "name": "Max the Dog",
        "species": "Golden Retriever",
        "personality": "The lovable goofball — always happy, always tail-wagging",
        "male": {
            "visual": (
                "A cheerful, fluffy anthropomorphic golden retriever with shiny golden-blonde fur, "
                "adorable floppy ears, a big wet black nose, and the happiest smile with tongue "
                "slightly out. He has warm brown puppy-dog eyes and a constantly wagging tail. "
                "He wears a vibrant orange Hawaiian shirt with tropical flower prints, "
                "cool khaki cargo shorts, fresh green high-top sneakers, and a fun red bandana "
                "tied around his neck. Cute 3D cartoon style, joyful and energetic."
            ),
            "image_prompt": (
                "Full body portrait of a cute happy anthropomorphic male golden retriever character, "
                "standing upright, fluffy golden fur, floppy ears, black nose, big happy smile, "
                "tongue out, brown eyes, wagging tail, wearing orange Hawaiian shirt, khaki shorts, "
                "green sneakers, red bandana. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, fun happy musician look."
            ),
        },
        "female": {
            "visual": (
                "A cheerful, fluffy anthropomorphic golden retriever with shiny golden-blonde fur, "
                "adorable floppy ears with a cute scrunchie, a small black nose, and the sweetest "
                "smile. She has warm sparkly brown eyes and a happy wagging tail with a bow. "
                "She wears a cute sunflower-print sundress, a trendy denim vest with enamel pins, "
                "and yellow canvas sneakers. She has a daisy flower crown and colorful beaded "
                "anklets. Cute 3D cartoon style, joyful and adorable."
            ),
            "image_prompt": (
                "Full body portrait of a cute happy anthropomorphic female golden retriever character, "
                "standing upright, fluffy golden fur, floppy ears with scrunchie, sparkly brown eyes, "
                "sweet smile, tail with bow, wearing sunflower sundress, denim vest with pins, "
                "yellow sneakers, daisy flower crown, beaded anklets. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cute adorable musician look."
            ),
        },
    },
    "jazz_rabbit": {
        "name": "Jazz the Rabbit",
        "species": "Dutch Rabbit",
        "personality": "The witty intellectual — sophisticated rhythm, cool confidence",
        "male": {
            "visual": (
                "A tall, slim anthropomorphic rabbit with soft white fur and cute black patches "
                "over both eyes and on his long upright ears. He has big expressive violet eyes, "
                "a tiny cute pink twitching nose, and a charming smile. "
                "He wears a vintage emerald green velvet blazer over a crisp white turtleneck, "
                "slim black trousers, and polished tan oxford shoes. "
                "He has cute round gold-rimmed glasses and a pocket square with music notes. "
                "Cute 3D cartoon style, sophisticated and friendly."
            ),
            "image_prompt": (
                "Full body portrait of a cute sophisticated anthropomorphic male Dutch rabbit character, "
                "standing upright, white fur with black eye patches and ear patches, long upright ears, "
                "violet eyes, pink nose, charming smile, wearing emerald velvet blazer, white turtleneck, "
                "black trousers, tan oxfords, gold-rimmed glasses, music note pocket square. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cool intellectual musician look."
            ),
        },
        "female": {
            "visual": (
                "A tall, graceful anthropomorphic rabbit with soft white fur and cute black patches "
                "over both eyes and on her long upright ears with pink insides. She has big sparkling "
                "violet eyes with long lashes, a tiny cute pink nose, and an elegant smile. "
                "She wears a chic emerald green wrap dress with a subtle shimmer, sheer black "
                "tights, and elegant tan heeled ankle boots. "
                "She has adorable round gold-rimmed glasses and a small pearl hair clip. "
                "Cute 3D cartoon style, elegant and charming."
            ),
            "image_prompt": (
                "Full body portrait of a cute elegant anthropomorphic female Dutch rabbit character, "
                "standing upright, white fur with black eye patches, long ears with pink insides, "
                "violet eyes with lashes, pink nose, elegant smile, wearing emerald wrap dress, "
                "sheer tights, tan heeled boots, gold-rimmed glasses, pearl hair clip. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, chic musician look."
            ),
        },
    },
    "spike_hedgehog": {
        "name": "Spike the Hedgehog",
        "species": "Hedgehog",
        "personality": "The fun punk rocker — small, spunky, full of playful energy",
        "male": {
            "visual": (
                "A small, adorable anthropomorphic hedgehog with soft brown spines styled upward "
                "with electric-blue tips like a fun mohawk, a cute tan belly and face, tiny round ears, "
                "and bright playful green eyes. He has a small cute pointy snout with a button nose. "
                "He wears a cool black band tee with a colorful lightning bolt, fun red plaid pants, "
                "and chunky pastel-blue sneakers with neon laces. "
                "He has a fun chain keychain and colorful rubber bracelets. "
                "Cute 3D cartoon style, playful punk energy, small and adorable."
            ),
            "image_prompt": (
                "Full body portrait of a cute small anthropomorphic male hedgehog character, "
                "standing upright, brown spines with blue tips styled up, tan face and belly, "
                "bright green eyes, button nose, happy expression, wearing black lightning bolt tee, "
                "red plaid pants, pastel-blue chunky sneakers, chain keychain, rubber bracelets. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, fun punk musician look, small and cute."
            ),
        },
        "female": {
            "visual": (
                "A small, adorable anthropomorphic hedgehog with soft brown spines styled with "
                "fun pink and purple streaks, a cute tan face and belly, tiny round ears with "
                "small hoop earrings, and bright playful green eyes with sparkly lashes. "
                "She has a small cute snout with a pink button nose. "
                "She wears a cute black crop top with a rainbow lightning bolt, a fun plaid "
                "mini skirt in pink and black, striped thigh-high socks, and chunky pink platform "
                "boots. She has a stack of colorful jelly bracelets. "
                "Cute 3D cartoon style, playful punk energy, small and adorable."
            ),
            "image_prompt": (
                "Full body portrait of a cute small anthropomorphic female hedgehog character, "
                "standing upright, brown spines with pink and purple streaks, tan face, green eyes "
                "with sparkly lashes, pink nose, cute expression, wearing black rainbow lightning "
                "crop top, pink plaid mini skirt, striped thigh-high socks, pink platform boots, "
                "jelly bracelets, small hoop earrings. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, fun punk musician look, small and cute."
            ),
        },
    },
    "coco_panda": {
        "name": "Coco the Panda",
        "species": "Giant Panda",
        "personality": "The sweet heartthrob — adorable, cuddly, everyone's favorite",
        "male": {
            "visual": (
                "A round, cuddly anthropomorphic giant panda with fluffy black and white fur, "
                "classic black eye patches, round black ears, and a plump white belly. "
                "He has large sparkling dark brown eyes with a gentle dreamy expression and a sweet smile. "
                "He wears a cozy pastel blue hoodie with a cute strawberry patch, "
                "comfortable light gray joggers, and clean white sneakers with blue accents. "
                "He has a fun enamel pin collection on his hoodie. "
                "Cute 3D cartoon style, soft and cuddly, warm and friendly."
            ),
            "image_prompt": (
                "Full body portrait of a cute cuddly anthropomorphic male giant panda character, "
                "standing upright, black and white fur, black eye patches, round ears, big brown eyes, "
                "sweet smile, plump belly, wearing pastel blue hoodie with strawberry patch, "
                "gray joggers, white sneakers, enamel pins on hoodie. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, adorable cozy musician look."
            ),
        },
        "female": {
            "visual": (
                "A round, cuddly anthropomorphic giant panda with fluffy black and white fur, "
                "classic black eye patches, round black ears, and a plump white belly. "
                "She has large sparkling dark brown eyes with long cute lashes and a sweet dimpled smile. "
                "She wears a cute pastel pink hoodie with a strawberry embroidered on the chest, "
                "an adorable light blue denim overall dress, and white platform sneakers with pink laces. "
                "She has a small flower hairpin behind her left ear and a heart-shaped locket necklace. "
                "Cute 3D cartoon style, soft and cuddly, warm and friendly."
            ),
            "image_prompt": (
                "Full body portrait of a cute cuddly anthropomorphic female giant panda character, "
                "standing upright, black and white fur, black eye patches, round ears, big brown eyes "
                "with lashes, dimpled smile, wearing pink hoodie, blue denim overall dress, "
                "white platform sneakers, flower hairpin, heart locket necklace. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, adorable cute musician look."
            ),
        },
    },
    "blaze_fox": {
        "name": "Blaze the Fox",
        "species": "Red Fox",
        "personality": "The charming showman — smooth, stylish, and full of flair",
        "male": {
            "visual": (
                "A sleek, handsome anthropomorphic red fox with vibrant orange-red fur, a fluffy "
                "white chest and chin, and a gorgeous bushy tail with a white tip. "
                "He has bright golden-amber eyes, cute pointed ears with black tips, and a charming "
                "confident smile. He wears a stylish navy blue blazer over a cool black V-neck tee, "
                "fitted dark jeans, and polished white Chelsea boots. "
                "He has trendy aviator sunglasses pushed up on his head and a sleek silver watch. "
                "Cute 3D cartoon style, suave and cool, friendly confidence."
            ),
            "image_prompt": (
                "Full body portrait of a cute handsome anthropomorphic male red fox character, "
                "standing upright, vibrant orange-red fur, white chest, bushy tail with white tip, "
                "golden-amber eyes, pointed ears, charming smile, wearing navy blazer, black tee, "
                "dark jeans, white Chelsea boots, aviator sunglasses on head, silver watch. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, suave cool musician look."
            ),
        },
        "female": {
            "visual": (
                "A sleek, gorgeous anthropomorphic red fox with vibrant orange-red fur, a fluffy "
                "white chest, and a fabulous bushy tail with a white tip tied with a small ribbon. "
                "She has bright golden-amber eyes with fluttery lashes, cute pointed ears with black "
                "tips, and a sweet confident smile. She wears a chic cropped navy blazer over a "
                "sparkly gold camisole, a stylish black mini skirt, and cute white ankle boots. "
                "She has heart-shaped rose-gold sunglasses and delicate gold hoop earrings. "
                "Cute 3D cartoon style, glamorous and fun, friendly confidence."
            ),
            "image_prompt": (
                "Full body portrait of a cute gorgeous anthropomorphic female red fox character, "
                "standing upright, vibrant orange-red fur, white chest, bushy tail with ribbon, "
                "golden-amber eyes with lashes, pointed ears, sweet smile, wearing cropped navy blazer, "
                "gold camisole, black mini skirt, white ankle boots, heart sunglasses, gold hoops. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, glamorous fun musician look."
            ),
        },
    },
    "ella_elephant": {
        "name": "Ella the Elephant",
        "species": "African Elephant",
        "personality": "The graceful soul — gentle, warm, and deeply musical",
        "male": {
            "visual": (
                "A tall, gentle anthropomorphic elephant with smooth soft gray skin, big friendly "
                "fan-shaped ears with pink inner edges, a cute long trunk, and small kind hazel eyes "
                "with a warm smile. He wears a stylish golden-yellow linen shirt with rolled-up sleeves, "
                "comfortable brown chino pants, and clean tan suede desert boots. "
                "He has a cool wooden bead bracelet and a small music note pin on his collar. "
                "Cute 3D cartoon style, gentle and warm, soft rounded features."
            ),
            "image_prompt": (
                "Full body portrait of a cute gentle anthropomorphic male African elephant character, "
                "standing upright, soft gray skin, big ears with pink edges, cute trunk, kind hazel eyes, "
                "warm smile, wearing golden-yellow linen shirt, brown chinos, tan desert boots, "
                "wooden bead bracelet, music note pin. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, gentle warm musician look."
            ),
        },
        "female": {
            "visual": (
                "A tall, graceful anthropomorphic elephant with smooth soft gray skin, big elegant "
                "fan-shaped ears with pink inner edges, a cute long trunk, and small kind hazel eyes "
                "with long lashes and a warm smile. She wears a flowing golden-yellow maxi dress "
                "with a fun colorful sash, chunky wooden bead bracelets on both wrists, "
                "and strappy tan sandals. She has a beautiful crown of wildflowers on her head. "
                "Cute 3D cartoon style, graceful and warm, soft rounded features."
            ),
            "image_prompt": (
                "Full body portrait of a cute graceful anthropomorphic female African elephant character, "
                "standing upright, soft gray skin, big ears with pink edges, cute trunk, hazel eyes "
                "with lashes, warm smile, wearing golden maxi dress, colorful sash, wooden bracelets, "
                "tan sandals, wildflower crown on head. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, graceful warm musician look."
            ),
        },
    },
    "ricky_raccoon": {
        "name": "Ricky the Raccoon",
        "species": "Raccoon",
        "personality": "The playful prankster — clever, fun, and surprisingly talented",
        "male": {
            "visual": (
                "A nimble, cute anthropomorphic raccoon with fluffy gray-brown fur, an adorable "
                "black mask marking around bright playful green eyes, and a bushy ringed tail. "
                "He has small rounded ears and cute hand-like paws. "
                "He wears a backwards bright red snapback cap, a baggy white graphic tee with a "
                "fun turntable print, comfy cargo pants, and classic checkered slip-on shoes. "
                "He has cool headphones around his neck and a fun wristband. "
                "Cute 3D cartoon style, playful and mischievous in a fun way."
            ),
            "image_prompt": (
                "Full body portrait of a cute playful anthropomorphic male raccoon character, "
                "standing upright, gray-brown fur, cute black mask markings, green eyes, bushy ringed tail, "
                "rounded ears, happy expression, wearing red snapback cap backwards, white turntable tee, "
                "cargo pants, checkered shoes, headphones around neck. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, fun playful musician look."
            ),
        },
        "female": {
            "visual": (
                "A nimble, cute anthropomorphic raccoon with fluffy gray-brown fur, an adorable "
                "black mask marking around bright sparkly green eyes with lashes, and a bushy ringed "
                "tail with a small bow. She has small rounded ears with tiny gem studs. "
                "She wears a cute oversized pink hoodie with a vinyl record print, a fun denim "
                "mini skirt, colorful striped knee socks, and white platform sneakers. "
                "She has sparkly headphones around her neck and stackable rings. "
                "Cute 3D cartoon style, playful and trendy."
            ),
            "image_prompt": (
                "Full body portrait of a cute playful anthropomorphic female raccoon character, "
                "standing upright, gray-brown fur, cute black mask markings, sparkly green eyes, "
                "bushy tail with bow, rounded ears with gem studs, happy expression, wearing pink "
                "hoodie with vinyl record print, denim mini skirt, striped knee socks, white platform "
                "sneakers, sparkly headphones. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, trendy playful musician look."
            ),
        },
    },
    "melody_owl": {
        "name": "Melody the Owl",
        "species": "Barn Owl",
        "personality": "The wise artist — mysterious charm with a gentle heart",
        "male": {
            "visual": (
                "A distinguished anthropomorphic barn owl with a cute heart-shaped white facial disc, "
                "soft golden-brown feathers with silver speckles, and large round warm dark eyes. "
                "He has a small neat beak and cute feathery ear tufts. "
                "He wears a stylish deep burgundy cardigan over a cream button-up shirt, "
                "neat dark brown corduroy pants, and polished leather lace-up boots. "
                "He has a vintage pocket watch chain and a small conductor's baton tucked in his pocket. "
                "Cute 3D cartoon style, wise and charming, gentle expression."
            ),
            "image_prompt": (
                "Full body portrait of a cute distinguished anthropomorphic male barn owl character, "
                "standing upright, heart-shaped white face, golden-brown feathers with silver speckles, "
                "warm dark eyes, small beak, ear tufts, wearing burgundy cardigan, cream shirt, "
                "brown corduroy pants, leather boots, pocket watch chain. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, wise charming musician look."
            ),
        },
        "female": {
            "visual": (
                "A graceful anthropomorphic barn owl with a cute heart-shaped white facial disc, "
                "soft golden-brown feathers with silver speckles, and large round warm dark eyes "
                "with long feathery lashes. She has a small delicate beak and cute ear tufts. "
                "She wears an elegant deep burgundy velvet cape over a cream lace blouse, "
                "a flowing dark skirt with musical note embroidery, and cute Victorian-style lace-up boots. "
                "She has a small sparkly tiara and a conductor's baton tucked in her belt. "
                "Cute 3D cartoon style, elegant and enchanting, gentle expression."
            ),
            "image_prompt": (
                "Full body portrait of a cute elegant anthropomorphic female barn owl character, "
                "standing upright, heart-shaped white face, golden-brown feathers, warm dark eyes "
                "with lashes, small beak, ear tufts, wearing burgundy velvet cape, cream lace blouse, "
                "dark skirt with music notes, Victorian boots, sparkly tiara. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, elegant enchanting musician look."
            ),
        },
    },
    "bubbles_frog": {
        "name": "Bubbles the Frog",
        "species": "Tree Frog",
        "personality": "The chill groove master — funky, relaxed, always vibing",
        "male": {
            "visual": (
                "A small, bouncy anthropomorphic tree frog with bright lime-green smooth skin, "
                "a pale yellow belly, and large adorable bulging orange eyes with a happy expression. "
                "He has wide cute webbed feet and sticky finger pads. "
                "He wears a fun tie-dye rainbow t-shirt, comfy purple harem pants, "
                "and cute open-toed sandals. He has a peace-sign necklace and a fun flower crown "
                "of daisies. His skin has a cute slight shimmer. "
                "Cute 3D cartoon style, groovy and chill, happy vibes."
            ),
            "image_prompt": (
                "Full body portrait of a cute bouncy anthropomorphic male tree frog character, "
                "standing upright, bright lime-green skin, yellow belly, big adorable orange eyes, "
                "wide webbed feet, happy expression, wearing tie-dye rainbow tee, purple harem pants, "
                "sandals, peace necklace, daisy flower crown. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, groovy chill musician look."
            ),
        },
        "female": {
            "visual": (
                "A small, bouncy anthropomorphic tree frog with bright lime-green smooth skin, "
                "a pale yellow belly, and large adorable bulging orange eyes with sparkly lashes. "
                "She has cute webbed feet and sticky finger pads. "
                "She wears a cute tie-dye cropped hoodie in pastel rainbow colors, a fun flowy "
                "purple skirt, and sparkly jelly sandals. She has a daisy chain necklace "
                "and tiny flower clips in a row on her head. Her skin has a cute shimmer. "
                "Cute 3D cartoon style, groovy and sweet, happy vibes."
            ),
            "image_prompt": (
                "Full body portrait of a cute bouncy anthropomorphic female tree frog character, "
                "standing upright, bright lime-green skin, yellow belly, big orange eyes with lashes, "
                "webbed feet, happy expression, wearing pastel tie-dye cropped hoodie, purple flowy "
                "skirt, sparkly jelly sandals, daisy chain necklace, flower clips on head. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, groovy sweet musician look."
            ),
        },
    },
    "thunder_wolf": {
        "name": "Thunder the Wolf",
        "species": "Gray Wolf",
        "personality": "The cool rockstar — confident, charismatic, heart of gold",
        "male": {
            "visual": (
                "A handsome, cool anthropomorphic gray wolf with fluffy silver-gray fur, a soft white "
                "chest, and a cute fluffy mane. He has friendly ice-blue eyes, a cute angular snout "
                "with a confident happy grin, and pointed fluffy ears. "
                "He wears a trendy long black coat over a clean white band tee, stylish fitted dark "
                "jeans, and cool black boots with silver buckles. "
                "He has a silver star pendant necklace and a fun wristband. "
                "Cute 3D cartoon style, cool rockstar vibes, friendly and approachable."
            ),
            "image_prompt": (
                "Full body portrait of a cute cool anthropomorphic male gray wolf character, "
                "standing upright, fluffy silver-gray fur, white chest, fluffy mane, friendly "
                "ice-blue eyes, happy confident grin, pointed ears, wearing black coat, white band tee, "
                "dark jeans, black boots with silver buckles, star pendant, wristband. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cool friendly rockstar look."
            ),
        },
        "female": {
            "visual": (
                "A beautiful, cool anthropomorphic gray wolf with fluffy silver-gray fur, a soft white "
                "chest, and a gorgeous fluffy mane styled with a cute side part. She has friendly "
                "ice-blue eyes with long lashes, a cute snout with a sweet confident smile, "
                "and pointed fluffy ears with small crystal studs. "
                "She wears a chic cropped black leather jacket over a sparkly white top, "
                "a stylish high-waisted dark skirt, and cute black ankle boots with silver chains. "
                "She has a delicate silver star pendant and a stack of thin silver bracelets. "
                "Cute 3D cartoon style, cool rockstar vibes, gorgeous and fun."
            ),
            "image_prompt": (
                "Full body portrait of a cute cool anthropomorphic female gray wolf character, "
                "standing upright, fluffy silver-gray fur, white chest, styled mane, ice-blue eyes "
                "with lashes, sweet smile, pointed ears with crystal studs, wearing cropped leather "
                "jacket, sparkly white top, dark skirt, black ankle boots, star pendant, silver bracelets. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, cool gorgeous rockstar look."
            ),
        },
    },
    "poppy_penguin": {
        "name": "Poppy the Penguin",
        "species": "Emperor Penguin",
        "personality": "The adorable showstopper — tiny, theatrical, born to perform",
        "male": {
            "visual": (
                "A short, adorable anthropomorphic emperor penguin with classic tuxedo black and white "
                "plumage, cute golden-yellow patches on the sides of his neck, and a bright orange beak. "
                "He has round shiny happy black eyes and cute small flipper-wings. "
                "He wears a sparkly silver sequin bow tie, a miniature tilted top hat, "
                "white gloves, and tiny shiny black tap shoes. He waddles with charm. "
                "Cute 3D cartoon style, theatrical and adorable, full of joy."
            ),
            "image_prompt": (
                "Full body portrait of a cute adorable anthropomorphic male emperor penguin character, "
                "standing upright, black and white tuxedo plumage, golden neck patches, orange beak, "
                "round happy black eyes, flipper-wings, wearing silver sequin bow tie, tilted top hat, "
                "white gloves, black tap shoes. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, theatrical adorable performer look."
            ),
        },
        "female": {
            "visual": (
                "A short, adorable anthropomorphic emperor penguin with classic tuxedo black and white "
                "plumage, cute golden-yellow patches, and a bright orange beak. "
                "She has round shiny sparkly black eyes with tiny lashes and cute flipper-wings. "
                "She wears a sparkly pink sequin bow, a tiny glittery tiara tilted to the side, "
                "a cute tutu skirt in pastel purple, and tiny sparkly ballet shoes. "
                "She has a small pearl bracelet. She waddles adorably. "
                "Cute 3D cartoon style, theatrical and precious, full of joy."
            ),
            "image_prompt": (
                "Full body portrait of a cute adorable anthropomorphic female emperor penguin character, "
                "standing upright, black and white plumage, golden patches, orange beak, sparkly eyes "
                "with lashes, wearing pink sequin bow, glittery tiara, pastel purple tutu, sparkly "
                "ballet shoes, pearl bracelet. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, theatrical precious performer look."
            ),
        },
    },
    "samba_parrot": {
        "name": "Samba the Parrot",
        "species": "Scarlet Macaw",
        "personality": "The fabulous entertainer — colorful, joyful, life of the party",
        "male": {
            "visual": (
                "A vibrant, fabulous anthropomorphic scarlet macaw with brilliant red feathers, "
                "bright blue and sunny yellow wing feathers, and a long colorful tail. "
                "He has a cute curved beak, round white eye patches with friendly dark eyes, "
                "and a fun feathered crest. He wears a flashy gold sequin jacket open at the front "
                "showing his red chest feathers, white bell-bottom pants, and shiny gold platform "
                "boots. He has fun gold rings and a feathered boa scarf. "
                "Cute 3D cartoon style, flamboyant and joyful, party energy."
            ),
            "image_prompt": (
                "Full body portrait of a cute vibrant anthropomorphic male scarlet macaw character, "
                "standing upright, brilliant red feathers, blue and yellow wings, colorful tail, "
                "curved beak, friendly eyes, feathered crest, wearing gold sequin jacket, "
                "white bell-bottoms, gold platform boots, gold rings, feathered boa. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, fabulous party musician look."
            ),
        },
        "female": {
            "visual": (
                "A vibrant, fabulous anthropomorphic scarlet macaw with brilliant red feathers, "
                "bright blue and sunny yellow wing feathers, and a gorgeous colorful tail. "
                "She has a cute curved beak, round white eye patches with sparkly friendly eyes "
                "and lashes, and a glamorous feathered crest with a tiny gem clip. "
                "She wears a dazzling gold sequin mini dress, cute strappy gold heels, "
                "and a fun feathered boa in rainbow colors. She has sparkly bangles. "
                "Cute 3D cartoon style, glamorous and joyful, party energy."
            ),
            "image_prompt": (
                "Full body portrait of a cute glamorous anthropomorphic female scarlet macaw character, "
                "standing upright, brilliant red feathers, blue and yellow wings, colorful tail, "
                "curved beak, sparkly eyes with lashes, feathered crest with gem, wearing gold sequin "
                "mini dress, gold heels, rainbow feathered boa, sparkly bangles. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, glamorous party musician look."
            ),
        },
    },
    "indie_deer": {
        "name": "Indie the Deer",
        "species": "White-tailed Deer",
        "personality": "The dreamy artist — gentle, creative, hauntingly beautiful",
        "male": {
            "visual": (
                "A gentle, graceful anthropomorphic deer with soft tawny-brown fur, a white belly, "
                "cute white inner ears, and a small white tail. He has large warm doe-brown eyes "
                "with a dreamy expression, a small cute black nose, and elegant antlers wrapped with "
                "tiny twinkling fairy lights. He wears an oversized cozy mustard-yellow knit sweater, "
                "comfortable brown corduroy pants, and tan leather boots. "
                "He has a cute canvas messenger bag with band patches. "
                "Cute 3D cartoon style, gentle indie vibes, warm and dreamy."
            ),
            "image_prompt": (
                "Full body portrait of a cute gentle anthropomorphic male white-tailed deer character, "
                "standing upright, tawny-brown fur, white belly, large warm brown doe eyes, black nose, "
                "antlers with tiny fairy lights, wearing mustard knit sweater, brown corduroy pants, "
                "tan boots, canvas messenger bag with patches. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, gentle indie musician look."
            ),
        },
        "female": {
            "visual": (
                "A gentle, graceful anthropomorphic deer with soft tawny-brown fur, a white belly, "
                "cute white inner ears, and a small white tail. She has large warm sparkling doe-brown "
                "eyes with long lashes, a small cute black nose, and small elegant antlers decorated "
                "with tiny flowers and fairy lights. She wears a cozy oversized mustard-yellow knit "
                "sweater dress, cute brown ankle boots, and a woven friendship bracelet. "
                "She has a small canvas tote with band patches. "
                "Cute 3D cartoon style, gentle indie vibes, sweet and dreamy."
            ),
            "image_prompt": (
                "Full body portrait of a cute gentle anthropomorphic female white-tailed deer character, "
                "standing upright, tawny-brown fur, white belly, sparkling brown doe eyes with lashes, "
                "black nose, small antlers with flowers and fairy lights, wearing mustard sweater dress, "
                "brown ankle boots, friendship bracelet, canvas tote with patches. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, sweet indie musician look."
            ),
        },
    },
    "duke_crocodile": {
        "name": "Duke the Crocodile",
        "species": "Crocodile",
        "personality": "The smooth jazz cat — cool, laid-back, funky grooves",
        "male": {
            "visual": (
                "A cool, friendly anthropomorphic crocodile with bright olive-green bumpy skin, "
                "a lighter yellow-green belly, and a cute long snout with a relaxed happy grin "
                "showing a few fun teeth. He has warm friendly golden eyes and a cute long tail. "
                "He wears a sharp pastel mint-green suit with a fun patterned shirt underneath "
                "open at the collar, a gold pocket watch chain, and shiny two-tone oxford shoes. "
                "He has a cool gold ring and a fun fedora hat. "
                "Cute 3D cartoon style, smooth jazz vibes, friendly and cool."
            ),
            "image_prompt": (
                "Full body portrait of a cute cool anthropomorphic male crocodile character, "
                "standing upright, bright olive-green skin, yellow belly, cute snout with happy grin, "
                "warm golden eyes, long tail, wearing mint-green suit, patterned shirt, "
                "gold pocket watch, two-tone oxfords, gold ring, fedora hat. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, smooth jazz musician look, friendly expression."
            ),
        },
        "female": {
            "visual": (
                "A cool, stylish anthropomorphic crocodile with bright olive-green bumpy skin, "
                "a lighter yellow-green belly, and a cute long snout with a sweet happy smile. "
                "She has warm friendly golden eyes with cute lashes and a long tail with a bow. "
                "She wears a chic pastel mint-green pantsuit with a sparkly camisole underneath, "
                "cute gold kitten heels, and a dainty gold chain necklace. "
                "She has a small clutch purse and a cute pillbox hat. "
                "Cute 3D cartoon style, smooth jazz vibes, elegant and fun."
            ),
            "image_prompt": (
                "Full body portrait of a cute stylish anthropomorphic female crocodile character, "
                "standing upright, bright olive-green skin, yellow belly, cute snout with sweet smile, "
                "golden eyes with lashes, tail with bow, wearing mint-green pantsuit, sparkly camisole, "
                "gold kitten heels, gold necklace, pillbox hat, clutch purse. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, elegant jazz musician look, friendly expression."
            ),
        },
    },
    "pixel_chameleon": {
        "name": "Pixel the Chameleon",
        "species": "Panther Chameleon",
        "personality": "The creative genius — innovative, quirky, visually dazzling",
        "male": {
            "visual": (
                "A quirky, eye-catching anthropomorphic chameleon with fun color-shifting skin in "
                "swirling patterns of electric blue, hot pink, and neon green. He has large cute "
                "turret-like eyes, a curled prehensile tail, and funny split-toed feet. "
                "He wears a cool futuristic silver jacket with glowing LED trim, fun holographic "
                "pants that shimmer with rainbow colors, and transparent light-up sneakers. "
                "He has tiny fun headphones built into his head crest. "
                "Cute 3D cartoon style, futuristic and fun, creative energy."
            ),
            "image_prompt": (
                "Full body portrait of a cute quirky anthropomorphic male panther chameleon character, "
                "standing upright, color-shifting skin in blue pink and green swirls, large turret eyes, "
                "curled tail, split-toed feet, wearing silver futuristic jacket with LED trim, "
                "holographic rainbow pants, transparent light-up sneakers, headphones in head crest. "
                "3D Pixar-style cartoon, vibrant neon colors, studio lighting, white background, "
                "full body visible, futuristic creative musician look."
            ),
        },
        "female": {
            "visual": (
                "A quirky, dazzling anthropomorphic chameleon with fun color-shifting skin in "
                "swirling patterns of pastel pink, lavender, and mint green. She has large cute "
                "turret-like eyes with sparkly lashes, a curled prehensile tail with a glowing tip, "
                "and funny split-toed feet. She wears a cute holographic crop jacket, "
                "a fun iridescent skater skirt, and transparent platform boots with LED lights inside. "
                "She has a glowing flower clip on her head crest. "
                "Cute 3D cartoon style, futuristic and dazzling, creative energy."
            ),
            "image_prompt": (
                "Full body portrait of a cute dazzling anthropomorphic female panther chameleon character, "
                "standing upright, color-shifting skin in pastel pink lavender and mint swirls, "
                "large turret eyes with sparkly lashes, curled tail with glowing tip, "
                "wearing holographic crop jacket, iridescent skater skirt, transparent LED platform boots, "
                "glowing flower clip on head crest. "
                "3D Pixar-style cartoon, vibrant pastel neon colors, studio lighting, white background, "
                "full body visible, futuristic creative musician look."
            ),
        },
    },
    "rosie_flamingo": {
        "name": "Rosie the Flamingo",
        "species": "Flamingo",
        "personality": "The glamorous star — elegant, dramatic, a voice like honey",
        "male": {
            "visual": (
                "A tall, elegant anthropomorphic flamingo with vibrant coral-pink plumage, "
                "long graceful legs, and a stylishly curved neck. He has a distinctive pink beak "
                "with a black tip, bright friendly yellow eyes, and smooth wing-arms. "
                "He wears a sharp white tuxedo jacket with a coral-pink pocket square, "
                "slim black pants, and polished white dress shoes. "
                "He has a sleek bow tie and a fun rose boutonniere. "
                "Cute 3D cartoon style, elegant showman, tall and graceful."
            ),
            "image_prompt": (
                "Full body portrait of a cute elegant anthropomorphic male flamingo character, "
                "standing upright, coral-pink plumage, long legs, curved neck, pink beak, "
                "friendly yellow eyes, wearing white tuxedo jacket, pink pocket square, "
                "black pants, white dress shoes, bow tie, rose boutonniere. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, elegant showman musician look."
            ),
        },
        "female": {
            "visual": (
                "A tall, stunning anthropomorphic flamingo with vibrant coral-pink plumage, "
                "long graceful legs, and a elegantly curved neck. She has a pretty pink beak "
                "with a black tip, bright sparkly yellow eyes with glamorous lashes, "
                "and elegant wing-arms with deeper magenta feathers. "
                "She wears a gorgeous black cocktail dress with a high slit, a long pearl necklace, "
                "elegant black satin gloves, and strappy gold stiletto heels. "
                "She has a red rose tucked behind her ear. "
                "Cute 3D cartoon style, glamorous diva, tall and stunning."
            ),
            "image_prompt": (
                "Full body portrait of a cute glamorous anthropomorphic female flamingo character, "
                "standing upright, coral-pink plumage, long legs, curved neck, pretty beak, "
                "sparkly yellow eyes with lashes, magenta wing feathers, wearing black cocktail dress, "
                "pearl necklace, black satin gloves, gold stiletto heels, red rose behind ear. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, glamorous diva musician look."
            ),
        },
    },
    "banjo_monkey": {
        "name": "Banjo the Monkey",
        "species": "Capuchin Monkey",
        "personality": "The hyperactive wildcard — chaotic fun, pure joy, endless tricks",
        "male": {
            "visual": (
                "A small, hyperactive anthropomorphic capuchin monkey with soft brown fur, "
                "a cute lighter cream face and chest, and a long curling prehensile tail. "
                "He has large round curious brown eyes, big expressive ears, and a wide cheeky grin. "
                "He wears a bright yellow newsboy cap, a fun red-and-white striped vest over a "
                "white tee, cute patched-up brown shorts, and no shoes (nimble bare feet). "
                "He has a harmonica on a holder around his neck. "
                "Cute 3D cartoon style, hyperactive and playful, pure joy."
            ),
            "image_prompt": (
                "Full body portrait of a cute hyperactive anthropomorphic male capuchin monkey character, "
                "standing upright, brown fur, cream face, long curling tail, big curious brown eyes, "
                "big ears, cheeky grin, wearing yellow newsboy cap, red-white striped vest, white tee, "
                "patched brown shorts, bare feet, harmonica holder around neck. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, playful joyful musician look."
            ),
        },
        "female": {
            "visual": (
                "A small, hyperactive anthropomorphic capuchin monkey with soft brown fur, "
                "a cute lighter cream face and chest, and a long curling prehensile tail with a ribbon. "
                "She has large round sparkly brown eyes with lashes, big expressive ears with "
                "tiny cherry earrings, and an adorable cheeky grin. "
                "She wears a cute yellow beret, a fun red-and-white striped dress with a poufy skirt, "
                "striped knee socks, and little red mary-jane shoes. "
                "She has a tiny tambourine clipped to her belt. "
                "Cute 3D cartoon style, hyperactive and adorable, pure joy."
            ),
            "image_prompt": (
                "Full body portrait of a cute hyperactive anthropomorphic female capuchin monkey character, "
                "standing upright, brown fur, cream face, curling tail with ribbon, sparkly brown eyes "
                "with lashes, big ears with cherry earrings, cheeky grin, wearing yellow beret, "
                "red-white striped poufy dress, striped knee socks, red mary-janes, tambourine on belt. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, adorable joyful musician look."
            ),
        },
    },
    "aurora_snake": {
        "name": "Aurora the Snake",
        "species": "King Cobra",
        "personality": "The enchanting performer — mesmerizing, graceful, magical vibes",
        "male": {
            "visual": (
                "A graceful, enchanting anthropomorphic cobra with beautiful iridescent scales that "
                "shimmer between deep purple and emerald green. He has a cute expandable hood with "
                "pretty golden eye-spot patterns, friendly warm golden eyes, and a gentle expression. "
                "He wears a stylish deep purple velvet jacket with gold embroidery, a silk "
                "white cravat, and elegant gold arm cuffs with swirl patterns. "
                "His tail coils neatly beneath him. He has a small gold circlet on his hood. "
                "Cute 3D cartoon style, enchanting and elegant, friendly mystical vibes."
            ),
            "image_prompt": (
                "Full body portrait of a cute enchanting anthropomorphic male king cobra character, "
                "standing upright, iridescent purple and green scales, cute hood with golden eye spots, "
                "warm golden eyes, gentle friendly expression, wearing purple velvet jacket with gold "
                "embroidery, white silk cravat, gold arm cuffs, gold circlet on hood, coiled tail. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, elegant mystical musician look, NOT scary."
            ),
        },
        "female": {
            "visual": (
                "A graceful, enchanting anthropomorphic cobra with beautiful iridescent scales that "
                "shimmer between soft lavender and mint green. She has a cute expandable hood with "
                "pretty golden eye-spot patterns, friendly warm golden eyes with long lashes, "
                "and a sweet gentle expression. She wears a fitted lavender bodysuit with gold "
                "spiral patterns, elegant long gold arm cuffs shaped like vines, and a beautiful "
                "gold circlet crown with an amethyst gem on her hood. "
                "Her tail coils gracefully beneath her. "
                "Cute 3D cartoon style, enchanting and beautiful, friendly mystical vibes."
            ),
            "image_prompt": (
                "Full body portrait of a cute enchanting anthropomorphic female king cobra character, "
                "standing upright, iridescent lavender and mint green scales, cute hood with golden "
                "eye spots, warm golden eyes with lashes, sweet expression, wearing lavender bodysuit "
                "with gold spirals, gold vine arm cuffs, amethyst circlet crown on hood, coiled tail. "
                "3D Pixar-style cartoon, vibrant colors, studio lighting, white background, "
                "full body visible, beautiful mystical musician look, NOT scary."
            ),
        },
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


def build_band(size: int, assignments: dict[str, str] = None,
               vocal_gender: str = "male") -> list[dict]:
    """Build a band with animal characters assigned to roles.

    Args:
        size: Number of band members (3-8)
        assignments: Optional dict mapping role_id -> character_id
        vocal_gender: "male" or "female" — used for the vocalist,
                      other members get alternating genders for variety

    Returns:
        List of dicts with full role + character info for each band member.
    """
    assignments = assignments or {}
    roles = get_band_roles(size)
    band = []

    for i, role_id in enumerate(roles):
        char_id = assignments.get(role_id, DEFAULT_ASSIGNMENTS.get(role_id))
        role = BAND_ROLES[role_id]
        character = ANIMAL_CHARACTERS[char_id]

        # Determine gender for this member
        if role_id == "vocalist":
            gender = vocal_gender
        else:
            # Alternate genders for variety, or use provided assignment gender
            gender = "female" if i % 2 == 1 else "male"

        gender_data = character[gender]

        band.append({
            "role_id": role_id,
            "role": role,
            "character_id": char_id,
            "character_name": character["name"],
            "species": character["species"],
            "personality": character["personality"],
            "gender": gender,
            "visual": gender_data["visual"],
            "image_prompt": gender_data["image_prompt"],
        })

    return band


def build_band_prompt(band: list[dict]) -> str:
    """Build a full video prompt describing the entire band on stage."""
    member_descriptions = []
    for m in band:
        member_descriptions.append(
            f"{m['character_name']} ({m['species']}): {m['visual']} — "
            f"playing {m['role']['instrument']} at {m['role']['stage_position']}"
        )

    members_text = "; ".join(member_descriptions)

    return (
        f"A cute 3D Pixar-style cartoon animated music video of an anthropomorphic animal band "
        f"performing on a vibrant colorful festival stage with neon lights and confetti. "
        f"The band members are: {members_text}. "
        f"All characters are cute, friendly, cool, and fashionable. They are fully anthropomorphic, "
        f"standing upright, with joyful expressive faces and dynamic fun body movements. "
        f"High quality 3D cartoon animation, vibrant colors, dramatic fun stage lighting."
    )


def build_closeup_prompt(member: dict, scene: str = "") -> str:
    """Build a close-up video prompt for a single band member."""
    return (
        f"Close-up shot in a cute 3D Pixar-style cartoon music video. "
        f"{member['visual']} "
        f"This character is joyfully {member['role']['description']}. "
        f"The camera focuses on {member['character_name']} at {member['role']['stage_position']}, "
        f"showing their cute expressive face and fun dynamic movements. "
        f"High quality 3D cartoon animation, vibrant stage lighting, colorful bokeh background. "
        f"{scene}"
    )


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

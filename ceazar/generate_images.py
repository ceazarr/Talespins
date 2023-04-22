# import json
# import requests
# import io
# import base64
# from PIL import Image, PngImagePlugin
# from requests.auth import HTTPBasicAuth

# def generate_image(topic, width=512, height=768):
#     url = "http://129.187.105.32:7861"

#     # enter username, password here, important!
#     username = "NLPPP23"
#     password = "WDV&LDV"

#     basic = HTTPBasicAuth(username, password)

#     prompt = "A picture of " + topic
#     negative_prompt = "(text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated"
#     payload = {
#                     "enable_hr": False,
#                     "denoising_strength": 0,
#                     "firstphase_width": 0,
#                     "firstphase_height": 0,
#                     "hr_scale": 2,
#                     "hr_upscaler": "string",
#                     "hr_second_pass_steps": 0,
#                     "hr_resize_x": 0,
#                     "hr_resize_y": 0,
#                     "prompt": prompt,
#                     "styles": [
#                         "string"
#                     ],
#                     "seed": -1,
#                     "subseed": -1,
#                     "subseed_strength": 0,
#                     "seed_resize_from_h": -1,
#                     "seed_resize_from_w": -1,
#                     # "sampler_name": "Euler a",
#                     "batch_size": 1,
#                     "n_iter": 1,
#                     "steps": 50,
#                     "cfg_scale": 7.5,
#                     "width": width,
#                     "height": height,
#                     "restore_faces": False,
#                     "tiling": False,
#                     "do_not_save_samples": False,
#                     "do_not_save_grid": False,
#                     "negative_prompt": negative_prompt,
#                     "eta": 0,
#                     "s_churn": 0,
#                     "s_tmax": 0,
#                     "s_tmin": 0,
#                     "s_noise": 1,
#                     "override_settings": {},
#                     "override_settings_restore_afterwards": True,
#                     "script_args": [],
#                     #"sampler_index": "DPM++ SDE Karras",
#                     "sampler_index": "Euler a",
#                     "script_name": "",
#                     "send_images": True,
#                     "save_images": False,
#                     "alwayson_scripts": {}
#                 }

#     # send the request
#     response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload, auth=basic)
#     r = response.json()
#     load_r = json.loads(r['info'])
#     meta = load_r["infotexts"][0]

#     for i, img_data in enumerate(r['images']):
#         if ',' not in img_data:
#             continue
#         image = Image.open(io.BytesIO(base64.b64decode(img_data.split(",",1)[1])))
#         pnginfo = PngImagePlugin.PngInfo()
#         pnginfo.add_text("parameters", f"width={width}, height={height}, topic={topic}")
#         image.save(f"image{i}.jpg", format='JPEG')
    
#     return r['images'][0]
# import json
# import requests
# import io
# import base64
# from PIL import Image, PngImagePlugin
# from requests.auth import HTTPBasicAuth

# def generate_images(topics=["applications", "effects", "benefits"], width=512, height=768):
#     url = "http://129.187.105.32:7861"

#     # enter username, password here, important!
#     username = "NLPPP23"
#     password = "WDV&LDV"

#     basic = HTTPBasicAuth(username, password)
#     images = []

#     for i, topic in enumerate(topics):
#         prompt = f"A picture of {topic}"
#         negative_prompt = "(text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated"
#         payload = {
#                         "enable_hr": False,
#                         "denoising_strength": 0,
#                         "firstphase_width": 0,
#                         "firstphase_height": 0,
#                         "hr_scale": 2,
#                         "hr_upscaler": "string",
#                         "hr_second_pass_steps": 0,
#                         "hr_resize_x": 0,
#                         "hr_resize_y": 0,
#                         "prompt": prompt,
#                         "styles": [
#                             "string"
#                         ],
#                         "seed": -1,
#                         "subseed": -1,
#                         "subseed_strength": 0,
#                         "seed_resize_from_h": -1,
#                         "seed_resize_from_w": -1,
#                         # "sampler_name": "Euler a",
#                         "batch_size": 1,
#                         "n_iter": 1,
#                         "steps": 50,
#                         "cfg_scale": 7.5,
#                         "width": width,
#                         "height": height,
#                         "restore_faces": False,
#                         "tiling": False,
#                         "do_not_save_samples": False,
#                         "do_not_save_grid": False,
#                         "negative_prompt": negative_prompt,
#                         "eta": 0,
#                         "s_churn": 0,
#                         "s_tmax": 0,
#                         "s_tmin": 0,
#                         "s_noise": 1,
#                         "override_settings": {},
#                         "override_settings_restore_afterwards": True,
#                         "script_args": [],
#                         #"sampler_index": "DPM++ SDE Karras",
#                         "sampler_index": "Euler a",
#                         "script_name": "",
#                         "send_images": True,
#                         "save_images": False,
#                         "alwayson_scripts": {}
#                     }

#         # send the request
#         response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload, auth=basic)
#         r = response.json()
#         load_r = json.loads(r['info'])
#         meta = load_r["infotexts"][0]

#         for j, img_data in enumerate(r['images']):
#             if ',' not in img_data:
#                 continue
#             image = Image.open(io.BytesIO(base64.b64decode(img_data.split(",",1)[1])))
#             pnginfo = PngImagePlugin.PngInfo()
#             pnginfo.add_text("parameters", f"width={width}, height={height}, topic={topic}")
#             image.save(f"image{i}_{j}.jpg", format='JPEG')
#             images.append(img_data)
        ##################################################################
#     return images
# import os
# import openai

# # Set OpenAI credentials
# openai.api_key = "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"
# openai.organization = "org-umtU2aMACFq7eNAg7bptz37h"

#     # List available models
#     models = openai.Model.list()
#     print(models)

#     # Create image using OpenAI API
#     res = openai.Image.create(
#         prompt="{topic}, tilt shift, bokeh, voxel, very render, high resolution",
#         n=3,
#         size="512x512",
#     )

#     # Print the image URLs
#     for i in res["data"]:
#         print(i["url"])
###########################################################################
# import os
# import openai

# # Set OpenAI credentials
# openai.api_key = "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"
# openai.organization = "org-umtU2aMACFq7eNAg7bptz37h"

# # Get user input for prompt
# prompt = input("Enter text to image prompt: ")

# # Create image using OpenAI API
# res = openai.Image.create(
#     prompt=f"{prompt}, very render, high resolution",
#     n=3,
#     size="512x512",
# )

# # Print the image URLs
# for i in res["data"]:
#     print(i["url"])

import openai
import base64
import os
import pathlib as Path
# Set OpenAI credentials
openai.api_key = "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"
openai.organization = "org-umtU2aMACFq7eNAg7bptz37h"

def generate_images(topic):
    # Create image using OpenAI API
    res = openai.Image.create(
        prompt=f"{topic}, very render, high resolution",
        n=3,
        size="512x512",
        response_format = "b64_json"
    )
    for i in range(0, len(res["data"])):
        b64 = res["data"][i]["b64_json"]
        with open(f"static/webstory_ceazar/imgs/image{i}.jpg", "wb") as f:
            f.write(base64.urlsafe_b64decode(b64))

    # Return the image URLs
    # return [i["url"] for i in res["data"]]

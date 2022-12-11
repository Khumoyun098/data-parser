"""
    UzA parser
"""
url = "https://api.uza.uz/api/v1/posts/{post_id}"
#
# import aiohttp
# import asyncio
# import time
#
# start_time = time.time()
#
#
# async def get_post(session, url):
#     async with session.get(url, ssl=False) as resp:
#         post = await resp.json()
#         if resp.status == 200:
#             lang = post['lang']
#             if lang == 2:
#                 return post['id']
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#
#         tasks = []
#         for number in range(1000, 431916):
#             url = "https://api.uza.uz/api/v1/posts/{post_id}".format(post_id=number)
#             tasks.append(asyncio.ensure_future(get_post(session, url)))
#
#         original_post = await asyncio.gather(*tasks)
#         post_ids = []
#         for post in original_post:
#             post_ids.append(post)
#         with open("post_ids.txt", "w+") as f:
#             f.write(str(post_ids))
#
#
# asyncio.run(main())
# print("--- %s seconds ---" % (time.time() - start_time))

# def uza_post_finder(url: str, lang: int = 2) -> List[int]:
#     """
#     :param url:
#     :param lang: default 2 == "O'zbek"
#     :return:
#     """
#     post_ids = []
#     found = 1
#     count = 1
#     while found:
#         if count > 431916:
#             break
#         target = url.format(post_id=count)
#         r = session.get(url=target, headers={'user-agent': "Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 ("
#                                                            "KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"})
#         if r.status_code == 200:
#             print("success ID", count)
#             data = r.json()
#             lang = data['lang']
#             if lang == 2:
#                 post_ids.append(count)
#                 count += 1
#                 print("Count", count)
#         count += 1
#
#     return post_ids
#
#
# print(uza_post_finder(url=url))

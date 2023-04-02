import json
import bs4
import requests
import lxml
import os


def get_pages():
    for number in range(1, 11):
        with open(f"page{number}.html", 'w', encoding='utf-8') as file:

            cookies = {
                'PHPSESSID': 'c7a96a341163a2245b753e4e9c40a713',
                'yandex_gid': '213',
                '_csrf_csrf_token': 'PFnrg7M4pDUoQ4kIYmQeqD4t2ckeUEwysLZmI-MRmHA',
                'mobile': 'no',
                'desktop_session_key': '99573013aa6349041afda52a4541e3ea3d67f07620e0b74efa6011f517564f0ddcc9d0df7d20fee861b7f1f25a6ac2ad672533f5b14ee0d02ee61e6f431f3a84a71ba82c82dcdd910e4146a5f9259b794f878c139a22f43cd9fbd5632de20adb',
                'desktop_session_key.sig': 'akH_KLwQR1D68wXG0_BjJZRFq5I',
                'mda_exp_enabled': '1',
                'gdpr': '0',
                '_ym_uid': '1679603333757787770',
                'yandex_login': '',
                'i': 'Mp8UHNpWYRzLkm6DJAuo4+BsDcgtB71nSNl/Qd20nYErvFBUJCPAuFJHStFkeoOsxNtcIK+szKSiNtfJVDHxnu1j7vk=',
                'yandexuid': '5683745471676226461',
                'yuidss': '5683745471676226461',
                '_csrf': 'Xh8H0PxBAcOEU00YrnvYFrpS',
                'spravka': 'dD0xNjc5Njc4MDIxO2k9OTQuMjUuMjI5LjEwODtEPUJERjhBRkE4NEUxQUFCRTA1ODlCNUY1OEU1RDQzQUVGMDZBODQ4RTUwODE5NUM3NDVGODFFNUMyMkJFOEZDRTcxRDQ3OEU0MUI1NUM5MTU2MTZEQkIzQjlGNUEyO3U9MTY3OTY3ODAyMTI1MzUyNTg2NTtoPWE1MzAwYzJiYzkyZWRkODgwNjBjMmExN2JmNjFmNTAw',
                'my_perpages': '%5B%5D',
                'disable_server_sso_redirect': '1',
                '_yasc': 'MIcXuHsb/AqnthVG5xHl7Yo+NpgmrdzwmsJ1caTeclko5QkiyqSc9+9eGgIJWw==',
                'ya_sess_id': 'noauth:1679931464',
                'ys': 'c_chck.1445627610',
                'mda2_beacon': '1679931464065',
                'sso_status': 'sso.passport.yandex.ru:synchronized',
                '_ym_d': '1679931467',
                '_ym_isad': '2',
                'yp': '1680017867.yu.5683745471676226461',
                'ymex': '1682523467.oyu.5683745471676226461',
                'cycada': 'qAK5KnpAgin5givLkOt2k96eRzeLmaCqZs9xjNpYqDw=', #отличается
            }

            headers = {
                'authority': 'www.kinopoisk.ru',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
                'cache-control': 'max-age=0',
                # 'cookie': 'PHPSESSID=c7a96a341163a2245b753e4e9c40a713; yandex_gid=213; _csrf_csrf_token=PFnrg7M4pDUoQ4kIYmQeqD4t2ckeUEwysLZmI-MRmHA; mobile=no; desktop_session_key=99573013aa6349041afda52a4541e3ea3d67f07620e0b74efa6011f517564f0ddcc9d0df7d20fee861b7f1f25a6ac2ad672533f5b14ee0d02ee61e6f431f3a84a71ba82c82dcdd910e4146a5f9259b794f878c139a22f43cd9fbd5632de20adb; desktop_session_key.sig=akH_KLwQR1D68wXG0_BjJZRFq5I; mda_exp_enabled=1; gdpr=0; _ym_uid=1679603333757787770; yandex_login=; i=Mp8UHNpWYRzLkm6DJAuo4+BsDcgtB71nSNl/Qd20nYErvFBUJCPAuFJHStFkeoOsxNtcIK+szKSiNtfJVDHxnu1j7vk=; yandexuid=5683745471676226461; yuidss=5683745471676226461; _csrf=Xh8H0PxBAcOEU00YrnvYFrpS; spravka=dD0xNjc5Njc4MDIxO2k9OTQuMjUuMjI5LjEwODtEPUJERjhBRkE4NEUxQUFCRTA1ODlCNUY1OEU1RDQzQUVGMDZBODQ4RTUwODE5NUM3NDVGODFFNUMyMkJFOEZDRTcxRDQ3OEU0MUI1NUM5MTU2MTZEQkIzQjlGNUEyO3U9MTY3OTY3ODAyMTI1MzUyNTg2NTtoPWE1MzAwYzJiYzkyZWRkODgwNjBjMmExN2JmNjFmNTAw; my_perpages=%5B%5D; disable_server_sso_redirect=1; _yasc=MIcXuHsb/AqnthVG5xHl7Yo+NpgmrdzwmsJ1caTeclko5QkiyqSc9+9eGgIJWw==; ya_sess_id=noauth:1679931464; ys=c_chck.1445627610; mda2_beacon=1679931464065; sso_status=sso.passport.yandex.ru:synchronized; _ym_d=1679931467; _ym_isad=2; yp=1680017867.yu.5683745471676226461; ymex=1682523467.oyu.5683745471676226461; cycada=qAK5KnpAgin5givLkOt2k96eRzeLmaCqZs9xjNpYqDw=',
                'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            }

            params = {
                'page': f'{number}'
            }

            response = requests.get('https://www.kinopoisk.ru/lists/movies/top500/', params=params, cookies=cookies, headers=headers).text
            file.write(response)


def get_data_about_films_from_pages():
    get_pages()
    main_data_about_films = []
    for i in range(1, 11):
        f = open(f"page{i}.html", encoding='utf-8')
        f_r = f.read()
        soup = bs4.BeautifulSoup(f_r, 'lxml')
        h = soup.find_all('a')
        for i in range(len(h)):
            if str(h[i]).find('href="/film/') != -1 and str(h[i]).find('class="base-movie-main-info_link__YwtP1"') != -1:
                main_data_about_films.append(h[i])
        f.close()
    return main_data_about_films


def get_urls_of_films():
    list_of_data_about_films = get_data_about_films_from_pages()
    list_of_urls_films = []
    indexs = []
    for i in range(len(list_of_data_about_films)):
        indexs.append([str(list_of_data_about_films[i]).find('href="/film'), str(list_of_data_about_films[i]).find('><div class="base-movie-main-info_mainInfo__ZL_u3"')])
    for j in range(len(indexs)):
        list_of_urls_films.append('https://www.kinopoisk.ru/' + str(list_of_data_about_films[j])[indexs[j][0]+7:indexs[j][1]-1])
    return list_of_urls_films


def get_count_reviews_of_films():
    count_pages_of_reviews = []
    list_of_urls_reviews_films = get_urls_of_films()
    for i in range(len(list_of_urls_reviews_films)):
        list_of_urls_reviews_films[i] += 'reviews/'
    for j in range(len(list_of_urls_reviews_films)):

        cookies = {
            'mobile': 'no',
            'mda_exp_enabled': '1',
            '_ym_uid': '1679603333757787770',
            'yandex_login': '',
            'i': 'Mp8UHNpWYRzLkm6DJAuo4+BsDcgtB71nSNl/Qd20nYErvFBUJCPAuFJHStFkeoOsxNtcIK+szKSiNtfJVDHxnu1j7vk=',
            'yandexuid': '5683745471676226461',
            'yuidss': '5683745471676226461',
            'my_perpages': '%5B%5D',
            '_ym_isad': '2',
            'yp': '1680017867.yu.5683745471676226461',
            'ymex': '1682523467.oyu.5683745471676226461',
            'tc': '1',
            'mustsee_sort_v5': '01.10.200.21.31.41.121.131.51.61.71.81.91.101.111',
            'desktop_session_key': '232b3ec1906b45ce8e94f1c8cd5e57321c7fa7f6c21ffd8811d359253a725c46b2c51e497ede3e365af28e00916582430edecdd8f72cd8c1d884e69e30e8e4f47cad9a5f21341a091e48db050cd0ae568e0464fd02f39bd2e38e240bd4cd06a2',
            'desktop_session_key.sig': 'vCgvEUT8cOAR-d-W22RXVPJoitc',
            'sso_status': 'sso.passport.yandex.ru:synchronized',
            'gdpr': '0',
            'PHPSESSID': '06a5ab954c096f4d88ea76caa6b0c13f',
            'user_country': 'ru',
            'yandex_gid': '2',
            '_csrf_csrf_token': 'bAVBKK6n8tvexHak5gGQp2zG1K8V__Kdb83BmomE_6Y',
            'ya_sess_id': 'noauth:1679993455',
            'ys': 'c_chck.3497908634',
            'mda2_beacon': '1679993455425',
            '_ym_visorc': 'b',
            'spravka': 'dD0xNjc5OTk4MDcyO2k9MjE3LjE5Ny4xMS42MTtEPTM2MzQ0MjJEMzg2RjY1OTQyQ0I0NTA5NUU2MDRGQUM3QTQ2N0JEMkZBNjIwRDc1RkYzQjM1NzM4ODcxRDk4RUVBRkZCMTE0NjI0NENEMThBRDhGMEQyRjZBNTcyO3U9MTY3OTk5ODA3MjAxMjYyODc5OTtoPWUwNzc3NzcyOGNmN2MxZTk3NzY5NzA0OTA4YzVkZGQy',
            '_yasc': '7/fOhQvVI3e8+7hxmoE1VcDzP/YCzHVZnIYWht74/735DtDsszzqCWLBOdme/w==',
            'yandex_plus_metrika_cookie': 'true',
            '_ym_d': '1679998098',
            'cycada': 'PkZhXqfR8KWHGRm+Uhorgd6eRzeLmaCqZs9xjNpYqDw=',
        }

        headers = {
            'authority': 'www.kinopoisk.ru',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'PHPSESSID=c7a96a341163a2245b753e4e9c40a713; yandex_gid=213; _csrf_csrf_token=PFnrg7M4pDUoQ4kIYmQeqD4t2ckeUEwysLZmI-MRmHA; mobile=no; desktop_session_key=99573013aa6349041afda52a4541e3ea3d67f07620e0b74efa6011f517564f0ddcc9d0df7d20fee861b7f1f25a6ac2ad672533f5b14ee0d02ee61e6f431f3a84a71ba82c82dcdd910e4146a5f9259b794f878c139a22f43cd9fbd5632de20adb; desktop_session_key.sig=akH_KLwQR1D68wXG0_BjJZRFq5I; mda_exp_enabled=1; gdpr=0; _ym_uid=1679603333757787770; yandex_login=; i=Mp8UHNpWYRzLkm6DJAuo4+BsDcgtB71nSNl/Qd20nYErvFBUJCPAuFJHStFkeoOsxNtcIK+szKSiNtfJVDHxnu1j7vk=; yandexuid=5683745471676226461; yuidss=5683745471676226461; _csrf=Xh8H0PxBAcOEU00YrnvYFrpS; spravka=dD0xNjc5Njc4MDIxO2k9OTQuMjUuMjI5LjEwODtEPUJERjhBRkE4NEUxQUFCRTA1ODlCNUY1OEU1RDQzQUVGMDZBODQ4RTUwODE5NUM3NDVGODFFNUMyMkJFOEZDRTcxRDQ3OEU0MUI1NUM5MTU2MTZEQkIzQjlGNUEyO3U9MTY3OTY3ODAyMTI1MzUyNTg2NTtoPWE1MzAwYzJiYzkyZWRkODgwNjBjMmExN2JmNjFmNTAw; my_perpages=%5B%5D; ya_sess_id=noauth:1679931464; ys=c_chck.1445627610; mda2_beacon=1679931464065; sso_status=sso.passport.yandex.ru:synchronized; _ym_isad=2; yp=1680017867.yu.5683745471676226461; ymex=1682523467.oyu.5683745471676226461; user_country=ru; tc=1; _yasc=VTAJlArcEui7BlbLe2mK7+4QpNXzZ5AOAo9YtwdP6VONKOg/E/T+tJMQ3BHibA==; _ym_visorc=b; yandex_plus_metrika_cookie=true; cycada=7Q3QMrS3pTMhNH7FhkrBjt6eRzeLmaCqZs9xjNpYqDw=; _ym_d=1679937017',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

        response = requests.get(f'{list_of_urls_reviews_films[j]}', cookies=cookies, headers=headers)
        soup_of_positive = bs4.BeautifulSoup(response.text, 'lxml').find_all('li', class_="pos")
        soup_of_negative = bs4.BeautifulSoup(response.text, 'lxml').find_all('li', class_="neg")
        soup_of_neutral = bs4.BeautifulSoup(response.text, 'lxml').find_all('li', class_="neut")

        indexs_of_positive = [str(soup_of_positive).find('b>'), str(soup_of_positive).find('</b>')]
        indexs_of_negative = [str(soup_of_negative).find('b>'), str(soup_of_negative).find('</b>')]
        indexs_of_neutral = [str(soup_of_neutral).find('b>'), str(soup_of_neutral).find('</b>')]
        count_pages_of_reviews.append({'url': list_of_urls_reviews_films[j],
                                       'count_reviews_positive': int(str(soup_of_positive)[indexs_of_positive[0]+2:indexs_of_positive[1]] if str(soup_of_positive)[indexs_of_positive[0]+2:indexs_of_positive[1]] != '' else 0),
                                       'count_reviews_negative': int(str(soup_of_negative)[indexs_of_negative[0]+2:indexs_of_negative[1]] if str(soup_of_negative)[indexs_of_negative[0]+2:indexs_of_negative[1]] != '' else 0),
                                       'count_reviews_neutral': int(str(soup_of_neutral)[indexs_of_neutral[0]+2:indexs_of_neutral[1]] if str(soup_of_neutral)[indexs_of_neutral[0]+2:indexs_of_neutral[1]] != '' else 0)})

    return count_pages_of_reviews


def multiple_replace(target_str, replace_values):
    for i, j in replace_values.items():
        target_str = target_str.replace(i, j)
    return target_str


def get_reviews():
    try:
        os.mkdir("C:\\Users\\denis\\PycharmProjects\\pythonProject15\\_reviews")
    except FileExistsError:
        pass
    list_of_data_reviews = get_count_reviews_of_films()
    file_of_reviews = open(f"_reviews\_all.json", 'w', encoding='utf-8')
    reviews = []
    reviews_pol = []
    reviews_otr = []
    reviews_neut = []
    for i in range(len(list_of_data_reviews)):

        count_pages_positive = int(list_of_data_reviews[i]['count_reviews_positive']) // 200 + 1
        count_pages_negative = int(list_of_data_reviews[i]['count_reviews_negative']) // 200 + 1
        count_pages_neutral = int(list_of_data_reviews[i]['count_reviews_neutral']) // 200 + 1

        cookies = {
            'mobile': 'no',
            'mda_exp_enabled': '1',
            '_ym_uid': '1679603333757787770',
            'yandex_login': '',
            'i': 'Mp8UHNpWYRzLkm6DJAuo4+BsDcgtB71nSNl/Qd20nYErvFBUJCPAuFJHStFkeoOsxNtcIK+szKSiNtfJVDHxnu1j7vk=',
            'yandexuid': '5683745471676226461',
            'yuidss': '5683745471676226461',
            'my_perpages': '%5B%5D',
            'tc': '1',
            'mustsee_sort_v5': '01.10.200.21.31.41.121.131.51.61.71.81.91.101.111',
            'spravka': 'dD0xNjc5OTk4MDcyO2k9MjE3LjE5Ny4xMS42MTtEPTM2MzQ0MjJEMzg2RjY1OTQyQ0I0NTA5NUU2MDRGQUM3QTQ2N0JEMkZBNjIwRDc1RkYzQjM1NzM4ODcxRDk4RUVBRkZCMTE0NjI0NENEMThBRDhGMEQyRjZBNTcyO3U9MTY3OTk5ODA3MjAxMjYyODc5OTtoPWUwNzc3NzcyOGNmN2MxZTk3NzY5NzA0OTA4YzVkZGQy',
            '_csrf': 'GcPTiRp-RRN3sH9fkfaBB6TA',
            'ya_sess_id': 'noauth:1680084976',
            'ys': 'c_chck.1157110602',
            'mda2_beacon': '1680084976633',
            'sso_status': 'sso.passport.yandex.ru:synchronized',
            'desktop_session_key': '85bdd273ed9d080a9184bb83e891aa03a33ba33e6fc0d360559b30878fbf17dff39dc53ee68523c44047ccca4ae9896bec63516b98300dc87d6e39a1dca9236b4e0b0c6bd25b2bf2496e0703084efa3c92345a454e4bdb69a7813d65c2ace1b3',
            'desktop_session_key.sig': '4dh3qQ3uF56r1zTo-vZ-m-sQkno',
            'gdpr': '0',
            'yp': '1680171380.yu.5683745471676226461',
            'ymex': '1682676980.oyu.5683745471676226461',
            '_ym_isad': '2',
            'PHPSESSID': '53c907b1ccc53236c440d85d21865f5f',
            'user_country': 'ru',
            'yandex_gid': '213',
            '_csrf_csrf_token': '7o38ojSlMlqBm1d3vV1i9Hrwwzf-mvGdwGWj5axJeVU',
            '_yasc': 'H3ieuWuBjYC29SpyU9GNSFyztoHc5QyqhJBMACrJ9WK3z6TWeCG+JE9h0Pu4pw==',
            'yandex_plus_metrika_cookie': 'true',
            '_ym_visorc': 'b',
            '_ym_d': '1680090613',
            'cycada': 'xaeXgu+qTjgKK9F1s0HFQd6eRzeLmaCqZs9xjNpYqDw=',
        }

        headers = {
            'authority': 'www.kinopoisk.ru',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
            'cache-control': 'max-age=0',
            # 'cookie': 'mobile=no; mda_exp_enabled=1; _ym_uid=1679603333757787770; yandex_login=; i=Mp8UHNpWYRzLkm6DJAuo4+BsDcgtB71nSNl/Qd20nYErvFBUJCPAuFJHStFkeoOsxNtcIK+szKSiNtfJVDHxnu1j7vk=; yandexuid=5683745471676226461; yuidss=5683745471676226461; my_perpages=%5B%5D; tc=1; mustsee_sort_v5=01.10.200.21.31.41.121.131.51.61.71.81.91.101.111; spravka=dD0xNjc5OTk4MDcyO2k9MjE3LjE5Ny4xMS42MTtEPTM2MzQ0MjJEMzg2RjY1OTQyQ0I0NTA5NUU2MDRGQUM3QTQ2N0JEMkZBNjIwRDc1RkYzQjM1NzM4ODcxRDk4RUVBRkZCMTE0NjI0NENEMThBRDhGMEQyRjZBNTcyO3U9MTY3OTk5ODA3MjAxMjYyODc5OTtoPWUwNzc3NzcyOGNmN2MxZTk3NzY5NzA0OTA4YzVkZGQy; _csrf=GcPTiRp-RRN3sH9fkfaBB6TA; ya_sess_id=noauth:1680084976; ys=c_chck.1157110602; mda2_beacon=1680084976633; sso_status=sso.passport.yandex.ru:synchronized; desktop_session_key=85bdd273ed9d080a9184bb83e891aa03a33ba33e6fc0d360559b30878fbf17dff39dc53ee68523c44047ccca4ae9896bec63516b98300dc87d6e39a1dca9236b4e0b0c6bd25b2bf2496e0703084efa3c92345a454e4bdb69a7813d65c2ace1b3; desktop_session_key.sig=4dh3qQ3uF56r1zTo-vZ-m-sQkno; gdpr=0; yp=1680171380.yu.5683745471676226461; ymex=1682676980.oyu.5683745471676226461; _ym_isad=2; PHPSESSID=53c907b1ccc53236c440d85d21865f5f; user_country=ru; yandex_gid=213; _csrf_csrf_token=7o38ojSlMlqBm1d3vV1i9Hrwwzf-mvGdwGWj5axJeVU; _yasc=H3ieuWuBjYC29SpyU9GNSFyztoHc5QyqhJBMACrJ9WK3z6TWeCG+JE9h0Pu4pw==; yandex_plus_metrika_cookie=true; _ym_visorc=b; _ym_d=1680090613; cycada=xaeXgu+qTjgKK9F1s0HFQd6eRzeLmaCqZs9xjNpYqDw=',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        }

        replace_values = {'[': '', ']': '', '\r': '', '\n': '', '</b>': '', '<br/>': '', '\t': '', '<i>': '', '</i>': '', '<b>': '',
                          '<span class="_reachbanner_" itemprop="reviewBody">': ''}

        for j in range(1, count_pages_positive + 1):

            response = requests.get(f'https://www.kinopoisk.ru/film/{str(list_of_data_reviews[i]["url"])[30:-9]}/reviews/ord/date/status/good/perpage/200/page/{j}/', cookies=cookies,
                                    headers=headers).text
            soup = str(bs4.BeautifulSoup(response, 'lxml').find_all('span', class_="_reachbanner_"))
            soup_2 = multiple_replace(soup, replace_values)
            for y in range(len(soup_2.split('</span>,'))):
                sp = soup_2.split('</span>,')[y]
                reviews_pol.append(sp)


        for j in range(1, count_pages_negative + 1):

            response = requests.get(f'https://www.kinopoisk.ru/film/{str(list_of_data_reviews[i]["url"])[30:-9]}/reviews/ord/date/status/bad/perpage/200/page/{j}/', cookies=cookies,
                                    headers=headers).text
            soup = str(bs4.BeautifulSoup(response, 'lxml').find_all('span', class_="_reachbanner_"))
            soup_2 = multiple_replace(soup, replace_values)
            for y in range(len(soup_2.split('</span>,'))):
                sp = soup_2.split('</span>,')[y]
                reviews_otr.append(sp)

        for j in range(1, count_pages_neutral + 1):

            response = requests.get(f'https://www.kinopoisk.ru/film/{str(list_of_data_reviews[i]["url"])[30:-9]}/reviews/ord/date/status/neutral/perpage/200/page/{j}/', cookies=cookies,
                                    headers=headers).text
            soup = str(bs4.BeautifulSoup(response, 'lxml').find_all('span', class_="_reachbanner_"))
            soup_2 = multiple_replace(soup, replace_values)
            for y in range(len(soup_2.split('</span>,'))):
                sp = soup_2.split('</span>,')[y]
                reviews_neut.append(sp)

    slovar_pos = {"positive": reviews_pol}
    slovar_neg = {"negative": reviews_otr}
    slovar_neut = {"neutral": reviews_neut}
    reviews.append(slovar_pos)
    reviews.append(slovar_neg)
    reviews.append(slovar_neut)
    json.dump(reviews, file_of_reviews, indent=5, ensure_ascii=False)
    file_of_reviews.close()


def main():
  get_reviews()

main()


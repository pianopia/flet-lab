import flet as ft
from pytube import YouTube
import os
import ffmpeg
from pprint import pprint


def main(page: ft.Page):
    # Text Control 生成
    t = ft.Text(value="Youtube ダウンロード", color="green")
    # ページのコントロールリストに Control を追加
    page.controls.append(t)
    # ページを更新
    page.update()

    first_name = ft.TextField(label="Youtube URL", autofocus=True)
    last_name = ft.TextField(label="保存場所")
    greetings = ft.Column()

    def btn_click(e):
        video_url = first_name.value
        download_location = last_name.value
        myVideo = YouTube(video_url)
        myVideo.streams.get_by_itag(251).download(download_location)

        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        #last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("ダウンロード", on_click=btn_click),
        greetings,
    )

ft.app(target=main)

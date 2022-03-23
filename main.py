import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    return {
        "Welcome": "Setup Complete"
    }


@api.get("/api/calculate")
def calculate():
    return 2 + 2


@api.get("/api/speedtest")
def speedTest():
    import speedtest
    wifi = speedtest.Speedtest()
    servers = []
    print("Wifi Download Speed is ", wifi.download())
    print("Wifi Upload Speed is ", wifi.upload())
    print("Wifi best server is ", wifi.get_best_server())
    print("Wifi Download Speed is ", wifi.results.share())
    print("Wifi ping ", wifi.results.ping)

    return {
        "download": wifi.download(),
        "upload": wifi.upload(),
        "get_best_server": wifi.get_best_server(),
        "ping": wifi.results.ping,
        "result_share": wifi.results.share()
    }

# if __name__ == '__main__':
#     uvicorn.run(api)

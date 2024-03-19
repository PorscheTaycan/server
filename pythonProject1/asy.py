import asyncio  # 인력은 하나
import random

async def show(x): # 'async 는 비동기 함수이다' 라는 것을 알려주는 것임. 비동기 -> 동시에 일어나지 않고 한 번에 일어나는데 끝나는 시간만 다름.
    x = random.sample([1, 2, 3, 4, 5], k =1)
    await asyncio.sleep(x[0])
    print(x)
count = 0
async def main():
    await asyncio.gather(  # await는 asyncio와 함께 쓰임.
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count),
        show(count)

    )
asyncio.run(main())


# #이게 동기 -> 동시에 일어난다.
# def xx ():
#     print("123123")
# xx(1)
# xx(1)
# xx(1)
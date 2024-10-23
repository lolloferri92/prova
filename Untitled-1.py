import asyncio

from apscheduler.schedulers.asyncio import AsyncIOScheduler 

async def send_msg():
    print("Message to send")

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_msg, 'interval', seconds=5)
    scheduler.start()

    print('Scheduler started')

    try:
        # Keep the main coroutine running
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        # Handle graceful shutdown
        scheduler.shutdown()
        print("Scheduler shut down")

if __name__ == "__main__":
    asyncio.run(main())
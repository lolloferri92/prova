import gpiod, asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def send_msg():
    print("print dei 5 secondi")

async def send_msg2():
    print("print dei 7 secondi")


async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_msg, 'interval', seconds=5)
    scheduler.add_job(send_msg2, 'interval', seconds=7)
    
    try:
        scheduler.start()
        print('Scheduler started. Press Ctrl+C to exit.')
        
        # ciclo infinito
        while True: 
            a=1
            await asyncio.sleep(10)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        scheduler.shutdown()
        print("Scheduler shut down successfully.")

if __name__ == "__main__":
    asyncio.run(main())





import aiosqlite
import asyncio

async def async_fetch_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            print("[ASYNC] All users fetched.")
            return users

async def async_fetch_older_users():
    async with aiosqlite.connect('users.db') as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            users = await cursor.fetchall()
            print("[ASYNC] Users older than 40 fetched.")
            return users

async def fetch_concurrently():
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    print("\n[RESULTS] All Users:")
    for user in all_users:
        print(user)
    print("\n[RESULTS] Users older than 40:")
        print(user)

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())

if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        print("\nDemo interrupted by user. Goodbye!")

    except RuntimeError as e:
        if "cannot run the event loop while another loop is running" in str(e):
            print("Running main in existing event loop...")
            import nest_asyncio
            nest_asyncio.apply()
            asyncio.run(main())
        else:
            raise

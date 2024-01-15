<svelte:head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.0.2/dist/tailwind.min.css" rel="stylesheet">
</svelte:head>
<main class="flex items-center justify-center h-screen bg-gray-700">
    <div class="p-6 max-w-sm mx-auto bg-white rounded-xl shadow-md">
        <h2 class="text-lg text-center text-gray-700 font-semibold">Social Bias Labelling System</h2>
        <form class="mt-4">
            <div>
                <label for="email" class="block text-sm font-medium text-gray-700">信箱</label>
                <input type="email" id="email" name="email" required class="mt-1 p-2 border-2 border-gray-200 focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50 rounded-md shadow-sm w-full" placeholder="請輸入信箱">
            </div>
            <div class="mt-4">
                <label for="password" class="block text-sm font-medium text-gray-700">密碼</label>
                <input type="password" id="password" name="password" required class="mt-1 p-2 border-2 border-gray-200 focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50 rounded-md shadow-sm w-full" placeholder="請輸入密碼">
            </div>
            <div class="mt-6">
                <button type="submit" class="w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:border-blue-700 focus:ring focus:ring-blue-200 active:bg-blue-700 transition duration-150 ease-in-out">
                    登入
                </button>
            </div>
        </form>
    </div>
</main>

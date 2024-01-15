<!-- Navigation bar -->
<nav class="bg-white shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
            <div class="flex">
                <!-- Navigation items -->
            </div>
        </div>
    </div>
</nav>
<!-- Main content -->
<div class="py-6">
    <div class="max-w-6xl mx-auto sm:px-6 lg:px-8">
        <div class="bg-white overflow-hidden shadow-sm sm:rounded-lg">
            <div class="p-6 bg-white border-b border-gray-200">
                <!-- Target section -->
                <div class="mb-4">
                    <h2 class="text-xl font-semibold">Target</h2>
                    <div class="text-gray-600">Keywords</div>
                </div>
                <!-- Questions section -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <!-- Left column for information -->
                    <div class="flex justify-center items-center bg-gray-100">
                        邪惡博士
                        
                        <!-- Information content here -->
                    </div>
                    <!-- Right column for questions -->
                    <div>
                        <div class="mb-4">
                            <div class="font-bold">
                                <span>是否帶有偏見？</span>
                                <button class="mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-700">是</button>
                                <button class="mt-2 ml-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700">否</button>
                            </div>
                            <div class="relative bg-white p-4 rounded-lg shadow max-w-sm">
                                <div class="bubble-point"></div>
                                <p class="text-gray-800">
                                    一位思考者坐在書滿桌的房間裡，深陷沉思。房間中央的桌子上堆滿了書籍、報紙和地球儀。其中一本書的封面上寫著「文化偏見」。
                                </p>
                            </div>
                        </div>
                        <div class="mb-4">
                            <div class="font-bold">
                                <span>是否帶有惡意？</span>
                                <button class="mt-2 px-4 py-2 bg-green-500 text-white rounded hover:bg-green-700">是</button>
                                <button class="mt-2 ml-2 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-700">否</button>
                            </div>

                            <div class="relative bg-white p-4 rounded-lg shadow max-w-sm">
                                <div class="bubble-point"></div>
                                <p class="text-gray-800">
                                    一位思考者坐在書滿桌的房間裡，深陷沉思。房間中央的桌子上堆滿了書籍、報紙和地球儀。其中一本書的封面上寫著「文化偏見」。
                                </p>
                            </div>
                        </div>
                        <!-- Navigation buttons -->
                        <div class="flex mt-4">
                            <button class="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-700 mr-2">不確定</button>
                            <button class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-700 mr-2">下一題</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
    .bubble-point {
        position: absolute;
        top: -5px;
        left: 10%;
        width: 10px;
        height: 10px;
        background-color: white;
        transform: translateX(-50%) rotate(45deg);
        box-shadow: -2px -2px 2px #00000010;
    }
</style>
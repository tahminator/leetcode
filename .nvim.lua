-- Disable Java LSP and autocomplete in Neovim

vim.api.nvim_create_autocmd("LspAttach", {
	callback = function(args)
		local client = vim.lsp.get_client_by_id(args.data.client_id)
		if client and client.name == "jdtls" then
			client.stop()
		end
	end,
})

vim.api.nvim_create_autocmd("FileType", {
	pattern = "java",
	callback = function()
		-- Disable completion (nvim-cmp) for Java
		local status, cmp = pcall(require, "cmp")
		if status then
			cmp.setup.buffer({ enabled = false })
		end
	end,
})

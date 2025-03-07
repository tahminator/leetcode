vim.api.nvim_create_autocmd("LspAttach", {
	callback = function(args)
		local client = vim.lsp.get_client_by_id(args.data.client_id)
		if client then
			client.stop() -- Disable all LSP clients
		end
	end,
})

vim.api.nvim_create_autocmd("FileType", {
	pattern = "*", -- Apply to all file types
	callback = function()
		-- Disable completion (nvim-cmp) globally
		local status, cmp = pcall(require, "cmp")
		if status then
			cmp.setup({ enabled = false })
		end
	end,
})

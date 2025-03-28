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

		-- Disable LSP diagnostics
		vim.diagnostic.config({
			virtual_text = false,
			signs = false,
			underline = false,
			update_in_insert = false,
			severity_sort = false,
		})

		-- Hide diagnostic messages completely
		vim.lsp.handlers["textDocument/publishDiagnostics"] = function() end

		-- Disable hover popups
		vim.lsp.handlers["textDocument/hover"] = function() end

		-- Disable signature help popups
		vim.lsp.handlers["textDocument/signatureHelp"] = function() end

		-- Disable autoformatting
		vim.api.nvim_create_autocmd("BufWritePre", {
			callback = function()
				vim.lsp.buf.clear_references()
			end,
		})
	end,
})
